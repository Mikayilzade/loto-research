from dataclasses import dataclass


@dataclass(frozen=True)
class Scenario:
    face_spend: float
    commission_rate: float = 0.07
    wagering_loss_deduction_fraction: float = 0.90
    federal_corp_rate: float = 0.21
    nc_corp_rate: float = 0.02

    def calculate(self) -> dict[str, float]:
        guaranteed_prizes = self.face_spend
        commission = self.face_spend * self.commission_rate
        deductible_wagering_loss = self.face_spend * self.wagering_loss_deduction_fraction
        taxable_wagering_income = guaranteed_prizes - deductible_wagering_loss
        taxable_increment = taxable_wagering_income + commission
        simple_combined_rate = self.federal_corp_rate + self.nc_corp_rate
        income_tax = taxable_increment * simple_combined_rate
        pre_tax_surplus = commission
        after_tax_surplus = pre_tax_surplus - income_tax
        return {
            "face_spend": self.face_spend,
            "guaranteed_prizes": guaranteed_prizes,
            "commission": commission,
            "deductible_wagering_loss": deductible_wagering_loss,
            "taxable_wagering_income": taxable_wagering_income,
            "taxable_increment": taxable_increment,
            "simple_combined_rate": simple_combined_rate,
            "income_tax": income_tax,
            "pre_tax_surplus": pre_tax_surplus,
            "after_tax_surplus": after_tax_surplus,
            "after_tax_surplus_pct_face": after_tax_surplus / self.face_spend,
            "tax_rate_break_even": commission / taxable_increment,
        }


if __name__ == "__main__":
    for face in (50.0, 100.0):
        print(Scenario(face).calculate())
