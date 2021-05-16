from typing import Any
from ..models.rule_result import RuleResult

class BaseRule:

    def __init__(self, **inputs: Any):
        self.inputs: dict[str, Any] = inputs

    def execute(self) -> RuleResult:
        raise NotImplementedError('execute must be implemented')