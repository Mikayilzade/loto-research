"""H162: deterministic NJ Pick-3 Green Ball retailer commission scenarios."""

PAIR_OUTCOMES = 100
STAKE_PER_PAIR = 0.50
PAIR_PRIZE = 25.00
FORCED_DRAWS = 2
SALES_COMMISSION_RATE = 0.05
CASHING_COMMISSION_RATE = 0.0125

face_cost = PAIR_OUTCOMES * STAKE_PER_PAIR
prize_floor = FORCED_DRAWS * PAIR_PRIZE
sales_commission = face_cost * SALES_COMMISSION_RATE
cashing_commission = prize_floor * CASHING_COMMISSION_RATE

scenarios = [
    ("player_only", prize_floor, prize_floor - face_cost),
    ("retailer_sales_commission", prize_floor + sales_commission, prize_floor + sales_commission - face_cost),
    ("retailer_sales_plus_cashing", prize_floor + sales_commission + cashing_commission, prize_floor + sales_commission + cashing_commission - face_cost),
]

if __name__ == "__main__":
    print(f"face_cost={face_cost:.3f}")
    print(f"prize_floor={prize_floor:.3f}")
    for name, gross, profit in scenarios:
        print(f"{name},{gross:.3f},{profit:.3f},{gross/face_cost:.6f}")
