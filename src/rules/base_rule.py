from ..models.rule_result import RuleResult

class BaseRule:

    def __init__(self):
        pass

    def execute(self) -> RuleResult:
        raise NotImplementedError('execute must be implemented')