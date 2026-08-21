from math import comb

N = 80
DRAWN = 20
SPOTS = 4
PRIZE = {0: 0, 1: 0, 2: 1, 3: 3, 4: 100}

space = comb(N, SPOTS)
base_ev = 0.0
rows = []
for m in range(SPOTS + 1):
    count = comb(DRAWN, m) * comb(N - DRAWN, SPOTS - m)
    probability = count / space
    contribution = probability * PRIZE[m]
    base_ev += contribution
    rows.append((m, count, probability, PRIZE[m], contribution))

print(f'combination_space={space}')
for row in rows:
    print(row)
print(f'base_complete_cover_ratio={base_ev:.12f}')
print(f'universal_2x_ratio={2*base_ev:.12f}')
print(f'universal_3x_ratio={3*base_ev:.12f}')
print(f'break_even_multiplier={1/base_ev:.12f}')
