from enum import IntEnum
from typing import Optional


class Severity(IntEnum):
    CRITICAL = 5
    HIGH = 4
    MEDIUM = 3
    LOW = 2
    INFORMATION = 1
    UNKNOWN = 0

    @staticmethod
    def from_str(severity: str) -> Optional["Severity"]:
        return Severity.__members__.get(severity.upper())