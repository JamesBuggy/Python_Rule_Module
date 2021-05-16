from src import RuleResult, BaseRule

class SampleRuleOne(BaseRule):

    def __init__(self):
        pass

    def execute(self) -> RuleResult:
        print('sample rule one')
        return RuleResult(True)