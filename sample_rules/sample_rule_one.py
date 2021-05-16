from typing import Any
from src import RuleResult, BaseRule

class SampleRuleOne(BaseRule):

    def __init__(self, **inputs: Any):
        super().__init__(**inputs)

    def execute(self) -> RuleResult:
        print('sample rule one', self.inputs)
        return RuleResult(True)