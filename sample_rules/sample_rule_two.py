from typing import Any
from src import RuleResult, BaseRule

class SampleRuleTwo(BaseRule):

    required_inputs: list[str] = []

    def __init__(self, **inputs: Any) -> None:
        super().__init__(**inputs)

    def _execute(self) -> RuleResult:
        return RuleResult(True)