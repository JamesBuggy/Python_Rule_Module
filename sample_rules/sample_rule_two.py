from typing import Any
from src import RuleResult, BaseRule

class SampleRuleTwo(BaseRule):

    def __init__(self, **inputs: Any):
        super().__init__(**inputs)

    def execute(self) -> RuleResult:
        print('sample rule two', self.inputs)
        return RuleResult(True)