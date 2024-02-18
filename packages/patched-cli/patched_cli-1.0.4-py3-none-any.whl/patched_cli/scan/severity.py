from enum import IntEnum
from typing import Optional

from patched_cli.models.common import Severity


class SemgrepSeverity(IntEnum):
    CRITICAL = Severity.CRITICAL
    ERROR = Severity.HIGH
    WARNING = Severity.MEDIUM
    INFO = Severity.LOW
    STYLE = Severity.INFORMATION
    NONE = Severity.UNKNOWN

    @staticmethod
    def from_str(severity: str) -> Optional["SemgrepSeverity"]:
        return SemgrepSeverity.__members__.get(severity.upper())
