from src import RuleResult, BaseRule

class SampleRuleTwo(BaseRule):

    def __init__(self):
        pass

    def execute(self) -> RuleResult:
        print('sample rule two')
        return RuleResult(True)