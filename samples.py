from src import RuleChain
from sample_rules.sample_rule_one import SampleRuleOne
from sample_rules.sample_rule_two import SampleRuleTwo

if __name__ == '__main__':
    RuleChain() \
        .execute(SampleRuleOne) \
        .execute(SampleRuleTwo)