from typing import Any
from ..enums.rule_error_type import RuleErrorType

class RuleResult:

    def __init__(self, is_successful: bool, errors: dict[RuleErrorType, list[str]] = dict(), **outputs: Any) -> None:
        self.is_successful: bool = is_successful
        self.errors: dict[RuleErrorType, list[str]] = errors
        self.outputs: dict[str, Any] = outputs