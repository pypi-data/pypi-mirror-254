import ast
import dataclasses
from collections import defaultdict
from dataclasses import dataclass
from itertools import chain
from typing import Union
import tokenize

import ast_comments
from ast import FunctionDef, AsyncFunctionDef, ClassDef, Constant, Name, Call, Attribute, arg, AST, FormattedValue


_AST_NODE = Union[ast_comments.Comment, FunctionDef, AsyncFunctionDef, ClassDef, Constant, Name]

STR_BYTE_LITERALS = {"r", "u", "R", "U", "f", "F", "fr", "Fr", "fR", "FR", "rf", "rF", "Rf", "RF", "b", "B", "br", "Br",
                     "bR", "BR", "rb", "rB", "Rb", "RB"}


def _ast_enrich_parent(node: ast.AST):
    for child in ast_comments.iter_child_nodes(node):
        if getattr(node, 'parents', None) is None:
            child.parents = [node]
        else:
            child.parents = node.parents + [node]
        _ast_enrich_parent(child)


@dataclass(slots=True, order=True, frozen=True)
class NodeChange:
    """
    A class to represent a change to a node in the AST

    Attributes order matters for the comparison
    """
    node: AST = dataclasses.field(hash=False, compare=False)

    old_value: str = dataclasses.field(hash=False, compare=False)
    new_value: str = dataclasses.field(hash=False, compare=False)

    end: int = dataclasses.field(hash=True, compare=False)
    end_col: int = dataclasses.field(hash=True, compare=False)

    start: int = dataclasses.field(hash=True, compare=True)
    start_col: int = dataclasses.field(hash=True, compare=True)

    def apply_change(self, output: str) -> str:
        next_value = self.new_value
        start = self.start
        start_col = self.start_col
        end = self.end
        end_col = self.end_col
        lines = output.splitlines(keepends=True)

        node_type = type(self.node)
        if node_type is Constant:
            start_line = lines[start - 1]
            start_line = start_line[:start_col] + next_value
            end_line = lines[end - 1]
            end_line = end_line[end_col:]
            lines[start - 1: end] = [start_line, end_line]
            return ''.join(lines)
        if node_type is ast_comments.Comment:
            start_line = lines[start - 1]
            start_line = start_line[:start_col] + next_value + start_line[end_col:]
            lines[start - 1] = start_line
            return ''.join(lines)
        elif node_type is ClassDef:
            is_after_class = False
            line_gen = (i for i in lines[start - 1:end])
            for tokeninfo in tokenize.generate_tokens(line_gen.__next__):
                if not is_after_class and tokeninfo.type is tokenize.NAME and tokeninfo.string == 'class':
                    is_after_class = True
                elif is_after_class and tokeninfo.type is tokenize.NAME:
                    start += tokeninfo.start[0] - 1
                    start_col = tokeninfo.start[1]
                    end = start
                    end_col = tokeninfo.end[1]
                    break

        elif node_type is FunctionDef:
            is_after_def = False
            line_gen = (i for i in lines[start - 1:end])
            for tokeninfo in tokenize.generate_tokens(line_gen.__next__):
                if not is_after_def and tokeninfo.type is tokenize.NAME and tokeninfo.string == 'def':
                    is_after_def = True
                elif is_after_def and tokeninfo.type is tokenize.NAME and tokeninfo.string == self.old_value:
                    start += tokeninfo.start[0] - 1
                    start_col = tokeninfo.start[1]
                    end = start
                    end_col = tokeninfo.end[1]
                    break

        start_line = lines[start - 1]
        end_line = lines[end - 1]

        if node_type is arg:
            text = ''.join(lines[start - 1: end])
            before_end_len = len(''.join(lines[start - 1: end - 1]))
            text_end_col = before_end_len + end_col
            start_col = text.find(self.old_value, start_col, text_end_col)
            end_col = len(end_line) - (len(text) - start_col - len(self.old_value))

        if start == end:
            start_line = start_line.encode()
            start_line = start_line[:start_col] + next_value.encode() + start_line[end_col:]
            lines[start - 1] = start_line.decode()
        else:
            start_line = start_line.encode()
            start_line = start_line[:start_col] + next_value.encode()
            end_line = end_line.encode()
            end_line = end_line[end_col:]
            lines[start - 1: end] = [start_line.decode(), end_line.decode()]

        return ''.join(lines)


class Obfuscator(ast_comments.NodeVisitor):
    __DEFAULT_VALUE_FORMAT = '{prefix}_{name}_{count}_{suffix}'

    def __init__(self):
        self._dunder_names: set[str] = set(dir(type))
        self._builtins: set[str] = set(__builtins__.keys())
        self._imported_names: set[str] = set()
        self._transformation_map: dict[type[_AST_NODE], dict[str: str]] = defaultdict(dict)
        self._changes: set[NodeChange] = set()
        self._src = None

    def _backward_handle_attributes(self, node: Name):
        if not hasattr(node, 'parents'):
            return

        current_node = node
        while isinstance(current_node.parents[-1], Attribute):
            current_node = current_node.parents[-1]
            parent = current_node.parents[-1]

            search_type = None
            if isinstance(parent, Call) and parent.func is current_node:
                # to handle the case where a function/class constructor is called
                for ast_type in [FunctionDef, AsyncFunctionDef, ClassDef]:
                    if current_node.attr in self._transformation_map[ast_type].keys():
                        search_type = ast_type
            elif current_node.attr in self._transformation_map[Name].keys():
                search_type = Name

            if search_type is None:
                break

            start = current_node.lineno
            start_col = current_node.col_offset
            end = current_node.end_lineno
            end_col = current_node.end_col_offset
            old_value = current_node.attr
            for i, line in reversed(list(enumerate(self._src.splitlines(keepends=True)[start - 1: end]))):
                search_args = [0, len(line)]
                if i == 0:
                    search_args[0] = start_col

                if end == start + i:
                    search_args[1] = end_col
                possible_start_col = line.rfind(old_value, *search_args)
                if possible_start_col != -1:
                    start = start + i
                    end = start
                    start_col = possible_start_col
                    end_col = start_col + len(old_value)
                    break

            self._trace_changes(current_node, old_value, node_type=search_type,
                                start=start, start_col=start_col, end=end, end_col=end_col)

    def _trace_changes(self, node: ast.AST, node_value: str, *,
                       start: int | None = None,
                       start_col: int | None = None,
                       end: int | None = None,
                       end_col: int | None = None,
                       node_type: type[_AST_NODE] | None = None,
                       prefix: str = '', suffix: str = '',
                       value_format: str = __DEFAULT_VALUE_FORMAT) -> str:
        if node_type is None:
            node_type = type(node)

        if node_value not in self._transformation_map[node_type].keys():
            name = node_type.__name__
            count = len(self._transformation_map[node_type])
            next_value = value_format.format(prefix=prefix, name=name, count=count, suffix=suffix)
            self._transformation_map[node_type][node_value] = next_value
        else:
            next_value = self._transformation_map[node_type][node_value]

        change = NodeChange(node=node,
                            old_value=node_value,
                            new_value=next_value,
                            start=start if start is not None else node.lineno,
                            start_col=start_col if start is not None else node.col_offset,
                            end=end if start is not None else node.end_lineno,
                            end_col=end_col if start is not None else node.end_col_offset)

        self._changes.add(change)
        return next_value

    def visit_Import(self, node):
        for alias in node.names:
            self._imported_names.add(alias.asname if alias.asname is not None else alias.name)
        return self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self._imported_names.add(alias.asname if alias.asname is not None else alias.name)
        return self.generic_visit(node)

    def visit_Constant(self, node):
        if not isinstance(node.value, str) or len(node.value.strip()) == 0:
            return self.generic_visit(node)

        lines: list[str] = self._src.splitlines(keepends=True)
        relevant_line = lines[node.lineno - 1: node.end_lineno]
        if len(lines) == node.end_lineno:
            relevant_line[len(relevant_line) - 1] += '\n'

        line_iter = iter(lines)

        tokens = (tokeninfo
                  for tokeninfo in tokenize.generate_tokens(lambda: next(line_iter))
                  if tokeninfo.type is tokenize.STRING and
                  tokeninfo.start[0] >= node.lineno and tokeninfo.end[0] <= node.end_lineno)
        # ((tokeninfo.start[0] == node.lineno and tokeninfo.start[1] >= node.col_offset) or
        #  tokeninfo.start[0] > node.lineno) and
        # ((tokeninfo.end[0] == node.end_lineno and tokeninfo.end[1] >= node.end_col_offset) or
        #  tokeninfo.end[0] < node.end_lineno))

        for token in tokens:
            start = token.start[0]
            start_col = token.start[1]
            end = token.end[0]
            end_col = token.end[1]

            prefix = next((i for i in STR_BYTE_LITERALS if i == token.string[:len(i)]), '')
            quotes = next((char for char in token.string[len(prefix):] if char in ['"', "'"]))
            if token.string[len(prefix):].find(quotes * 3) == 0:
                quotes = quotes * 3

            joined_str_node = None
            if prefix != '':
                module = ast.parse(token.string, mode='eval')
                joined_str_node = module.body if isinstance(module.body, ast.JoinedStr) else None

            if joined_str_node is not None and len(joined_str_node.values) > 1:
                for i, value in enumerate(joined_str_node.values):
                    if (not isinstance(value, ast.Constant) or
                            not isinstance(value.value, str) or
                            len(value.value.strip()) == 0):
                        continue
                    node_kwargs = dict(start=start, start_col=start_col, end=end, end_col=end_col)
                    if i < len(joined_str_node.values) - 1:
                        formatting_node_after = joined_str_node.values[i + 1]  # type: FormattedValue
                        node_kwargs["end"] = formatting_node_after.value.lineno + start - 1
                        node_kwargs["end_col"] = formatting_node_after.value.col_offset + start_col - 1
                    if i > 0:
                        formatting_node_before = joined_str_node.values[i - 1]  # type: FormattedValue
                        node_kwargs["start"] = formatting_node_before.value.end_lineno + start - 1
                        node_kwargs["start_col"] = formatting_node_before.value.end_col_offset + start_col + 1

                    if i == 0:
                        node_kwargs["start_col"] += len(prefix) + len(quotes)
                    if i == len(joined_str_node.values) - 1:
                        node_kwargs["end_col"] -= len(quotes)

                    if node_kwargs["start"] == node_kwargs["end"]:
                        text = lines[node_kwargs["start"] - 1][node_kwargs["start_col"]:node_kwargs["end_col"]]
                    else:
                        start_line = lines[node_kwargs["start"] - 1][node_kwargs["start_col"]:]
                        between_lines = lines[node_kwargs["start"]: node_kwargs["end"] - 1]
                        end_line = lines[node_kwargs["end"] - 1][:node_kwargs["end_col"]]
                        text = ''.join([start_line, *between_lines, end_line])
                    self._trace_changes(node, text, **node_kwargs)
            else:
                text = token.string[len(prefix) + len(quotes): -len(quotes)]
                start_col += len(prefix) + len(quotes)
                end_col -= len(quotes)
                self._trace_changes(node, text, start=start, start_col=start_col, end=end, end_col=end_col)

        return self.generic_visit(node)

    def visit_Name(self, node):
        if node.id in self._imported_names or node.id in self._builtins:
            return self.generic_visit(node)

        search_type = Name
        parent = node.parents[-1]
        if isinstance(parent, Call) and parent.func is node:
            # to handle the case where a function/class constructor is called
            for ast_type in [FunctionDef, AsyncFunctionDef, ClassDef]:
                if node.id in self._transformation_map[ast_type].keys():
                    search_type = ast_type
        elif isinstance(parent, ClassDef) and any(base is node for base in parent.bases):
            # to handle the case where a class is defined as a base class of another class
            if node.id in self._transformation_map[ClassDef].keys():
                search_type = ClassDef

        current_node_id = node.id
        next_node_id = self._trace_changes(node, node.id, node_type=search_type)

        if current_node_id != next_node_id and isinstance(parent, Attribute):
            self._backward_handle_attributes(node)

        node.id = next_node_id
        return self.generic_visit(node)

    def visit_Comment(self, node):
        node.value = self._trace_changes(node, node.value, prefix='# ')
        return self.generic_visit(node)

    def _visit_function(self, node: FunctionDef | AsyncFunctionDef):
        if node.args is not None:
            for arg in chain(node.args.posonlyargs, node.args.args, node.args.kwonlyargs):
                arg.arg = self._trace_changes(arg, arg.arg, node_type=Name)

        if node.name in self._dunder_names:
            return self.generic_visit(node)

        node_type = FunctionDef if isinstance(node, FunctionDef) else AsyncFunctionDef
        node.name = self._trace_changes(node, node.name, node_type=node_type)
        return self.generic_visit(node)

    def visit_FunctionDef(self, node):
        return self._visit_function(node)

    def visit_AsyncFunctionDef(self, node):
        return self._visit_function(node)

    def visit_ClassDef(self, node):
        node.name = self._trace_changes(node, node.name)
        return self.generic_visit(node)

    def obfuscate(self, src: str) -> str:
        tree = ast_comments.parse(src)
        _ast_enrich_parent(tree)

        self._src = src
        self.visit(tree)
        self._src = None

        return self._commit_changes(src)

    def deobfuscate(self, src: str) -> str:
        tree = ast_comments.parse(src)
        _ast_enrich_parent(tree)

        deobfuscator = _Deobfuscator(self._transformation_map)
        deobfuscator._src = src
        deobfuscator.visit(tree)
        deobfuscator._src = None

        return deobfuscator._commit_changes(src)

    def _commit_changes(self, src):
        output = src
        for change in sorted(self._changes, reverse=True):
            output = change.apply_change(output)
        self._changes.clear()
        return output


class _Deobfuscator(Obfuscator):
    def __init__(self, transformation_map: dict[type, dict[str, str]]):
        super().__init__()
        self._transformation_map = defaultdict(dict)
        for node_type in transformation_map.keys():
            for k, v in transformation_map[node_type].items():
                self._transformation_map[node_type][v] = k

    def _trace_changes(self, node: ast.AST, node_value: str, *,
                       start: int | None = None,
                       start_col: int | None = None,
                       end: int | None = None,
                       end_col: int | None = None,
                       node_type: type[_AST_NODE] | None = None,
                       prefix: str = '', suffix: str = '',
                       value_format: str = "") -> None:
        if node_type is None:
            node_type = type(node)

        if node_type not in self._transformation_map.keys():
            return

        if node_value in self._transformation_map[node_type].keys():
            next_value = self._transformation_map[node_type][node_value]
        else:
            next_value = node_value

        change = NodeChange(node=node,
                            old_value=node_value,
                            new_value=next_value,
                            start=start if start is not None else node.lineno,
                            start_col=start_col if start is not None else node.col_offset,
                            end=end if start is not None else node.end_lineno,
                            end_col=end_col if start is not None else node.end_col_offset)

        self._changes.add(change)
