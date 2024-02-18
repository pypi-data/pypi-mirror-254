from enum import Enum
from typing import Generator, Protocol, Callable, Optional

from patched_cli.models.common import Vuln, Severity, VulnFile


class FilterKey(Enum):
    SEVERITY = "SEVERITY"
    CWE = "CWE"


class Comparator(Enum):
    EQ = "="


class FilterProtocol(Protocol):
    def apply(self, vuln: Vuln) -> bool:
        ...


class NoopFilter:
    def apply(self, vuln: Vuln) -> bool:
        return True


class Filter:
    def __init__(self, key: FilterKey, value: int | Severity):
        self._key = key
        self._value = value
        self._getter: Callable[[Vuln], Severity| int]
        if self._key == FilterKey.SEVERITY:
            self._getter = self._get_severity
        elif self._key == FilterKey.CWE:
            self._getter = self._get_cwe
        else:
            raise ValueError(f"Unknown filter key: {self._key}. Can only be one of {FilterKey.__members__.keys()}")

    def apply(self, vuln: Vuln) -> bool:
        return self._getter(vuln) == self._value

    @staticmethod
    def _get_severity(vuln: Vuln) -> Severity:
        return vuln.severity

    @staticmethod
    def _get_cwe(vuln: Vuln) -> int:
        return vuln.cwe.id

    @staticmethod
    def from_str(expr: str) -> Optional["Filter"]:
        for cmp_op in Comparator.__members__.values():
            if expr.count(cmp_op.value) == 1:
                key, delimiter, value = expr.partition(cmp_op.value)
                filter_key = FilterKey(key.strip().upper())
                filter_value: Severity | int | None
                if filter_key == FilterKey.SEVERITY:
                    try:
                        filter_value = Severity.from_str(value.strip().upper())
                        if filter_value is None:
                            raise ValueError("error")
                    except ValueError:
                        raise ValueError(f"Unknown severity: {value}. Can only be one of {Severity.__members__.keys()}")
                elif filter_key == FilterKey.CWE:
                    try:
                        filter_value = int(value.strip())
                    except ValueError:
                        raise ValueError(f"Unknown CWE: {value}. Must be an integer.")
                else:
                    raise ValueError(f"Unknown filter key: {filter_key}. "
                                     f"Can only be one of {FilterKey.__members__.keys()}")
                return Filter(filter_key, filter_value)
        return None


class Filters:
    def __init__(self, filters: list[FilterProtocol]):
        self._filters = filters

    def apply_vuln(self, data: list[Vuln]) -> Generator[Vuln, None, None]:
        for vuln in data:
            if all(_filter.apply(vuln) for _filter in self._filters):
                yield vuln

    def apply_vuln_file(self, data: list[VulnFile]) -> Generator[VulnFile, None, None]:
        for vuln_file in data:
            vuln_file.vulns = list(self.apply_vuln(vuln_file.vulns))
            if len(vuln_file.vulns) > 0:
                yield vuln_file

    @staticmethod
    def from_str_list(inputs: list[str]) -> "Filters":
        filters: list[FilterProtocol] = []
        for filter_str in inputs:
            filter_obj = Filter.from_str(filter_str)
            if filter_obj is None:
                continue
            filters.append(filter_obj)

        return Filters(filters)
