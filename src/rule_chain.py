from src.rules.base_rule import BaseRule
from typing import Type

class RuleChain:

    def __init__(self):
        pass

    def execute(self, rule: Type[BaseRule]) -> 'RuleChain':
        rule().execute()
        return self