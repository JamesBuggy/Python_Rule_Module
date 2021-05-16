from typing import Any
from rules_module import RuleResult, BaseRule

class SampleRuleOne(BaseRule):

    required_inputs: list[str] = []

    def __init__(self, **inputs: Any) -> None:
        super().__init__(**inputs)

    def _execute(self) -> RuleResult:
        return RuleResult(True)