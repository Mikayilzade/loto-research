"""H165: tax stress screen for NC Pick 3 forced Double Draw retailer overlay.

This is a conservative sensitivity calculator, not tax advice.
It reproduces the simple packet identity:
$50 wager -> $50 guaranteed prizes on forced Double Draw,
plus $3.50 retailer commission if commission-bearing.
Beginning 2026, federal wagering-loss deduction is capped at 90% of losses.
"""

FACE_SPEND = 50.0
GUARANTEED_PRIZES = 50.0
RETAILER_COMMISSION_RATE = 0.07
LOSS_DEDUCTION_FRACTION_2026 = 0.90
NC_RATE_2026 = 0.0399

commission = FACE_SPEND * RETAILER_COMMISSION_RATE
phantom_gambling_taxable = GUARANTEED_PRIZES - FACE_SPEND * LOSS_DEDUCTION_FRACTION_2026
combined_taxable_increment = phantom_gambling_taxable + commission
break_even_combined_rate = commission / combined_taxable_increment

print(f"commission={commission:.4f}")
print(f"phantom_gambling_taxable={phantom_gambling_taxable:.4f}")
print(f"combined_taxable_increment={combined_taxable_increment:.4f}")
print(f"break_even_combined_rate={break_even_combined_rate:.9%}")

for federal_rate in [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]:
    combined_rate = federal_rate + NC_RATE_2026
    after_tax = commission - combined_taxable_increment * combined_rate
    print(
        f"federal={federal_rate:.0%}, nc={NC_RATE_2026:.2%}, "
        f"simple_after_tax_profit={after_tax:.4f}"
    )
