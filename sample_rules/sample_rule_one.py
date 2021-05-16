from typing import Any
from src import RuleResult, BaseRule

class SampleRuleOne(BaseRule):

    required_inputs: 'list[str]' = []

    def __init__(self, **inputs: Any) -> None:
        super().__init__(**inputs)

    def execute(self) -> RuleResult:
        print('sample rule one', self.inputs)
        return RuleResult(True)