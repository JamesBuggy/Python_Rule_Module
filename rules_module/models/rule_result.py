from enum import Enum
from typing import Any

class RuleResult:

    def __init__(self, is_successful: bool, errors: dict[Enum, list[str]] = dict(), **outputs: Any) -> None:
        self.is_successful: bool = is_successful
        self.errors: dict[Enum, list[str]] = errors
        self.outputs: dict[str, Any] = outputs