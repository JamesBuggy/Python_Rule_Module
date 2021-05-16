from typing import Any
from ..enums.rule_error_type import RuleErrorType

class RuleResult:

    def __init__(self, is_successful: bool, errors: dict[RuleErrorType, list[str]] = dict(), **outputs: Any) -> None:
        self.is_successful = is_successful
        self.outputs: dict[str, Any] = outputs
        self.errors = errors