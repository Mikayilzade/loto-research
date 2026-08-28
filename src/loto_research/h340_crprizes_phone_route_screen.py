from dataclasses import dataclass

@dataclass(frozen=True)
class CAndRReferenceInstantPool:
    total_ids: int = 1000
    cash_500: int = 1
    cash_250: int = 2
    cash_100: int = 6
    cash_50: int = 5
    site_credit_15: int = 7
    site_credit_10: int = 30
    site_credit_5: int = 49

    @property
    def listed_prize_ids(self):
        return self.cash_500+self.cash_250+self.cash_100+self.cash_50+self.site_credit_15+self.site_credit_10+self.site_credit_5

    @property
    def withdrawable_cash_ids(self):
        return self.cash_500+self.cash_250+self.cash_100+self.cash_50

    @property
    def zero_instant_ids(self):
        return self.total_ids-self.listed_prize_ids


def validate():
    p=CAndRReferenceInstantPool()
    assert p.listed_prize_ids == 100
    assert p.withdrawable_cash_ids == 14
    assert p.zero_instant_ids == 900
    assert p.zero_instant_ids > 0
    # A random single identifier therefore has a legal £0 withdrawable-instant-cash outcome.
    return {
        'total_ids':p.total_ids,
        'listed_prize_ids':p.listed_prize_ids,
        'withdrawable_cash_ids':p.withdrawable_cash_ids,
        'site_credit_ids':86,
        'zero_instant_ids':p.zero_instant_ids,
        'arithmetic_inconclusive':0,
    }

if __name__=='__main__':
    print(validate())
