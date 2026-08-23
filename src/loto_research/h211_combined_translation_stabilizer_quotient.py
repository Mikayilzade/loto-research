"""H211 exact combination of H210 residual translations with H191 stabilizers.

H210: C16 acts freely on every 3-layer A subset, giving C(128,3)/16 A-orbits.
H191: only A-layers with a=15 are fully S3-compatible; 3-subsets entirely
inside that 16-layer sector can use 15 B/C coefficient classes instead of 36.

Because H210 preserves coefficient a and acts freely also on the a=15 sector,
its exceptional C(16,3) subsets split into exactly C(16,3)/16=35 orbits.
The remaining A subsets split into (C(128,3)-C(16,3))/16 generic orbits.
Therefore the exact combined quotient is
  generic_orbits*36 + exceptional_orbits*15 = 767,361.
"""
from math import comb

ALL_A = comb(128, 3)
EXCEPTIONAL_A = comb(16, 3)
GENERIC_A = ALL_A - EXCEPTIONAL_A


def main():
    assert ALL_A % 16 == 0
    assert EXCEPTIONAL_A % 16 == 0
    assert GENERIC_A % 16 == 0
    all_orbits = ALL_A // 16
    exceptional_orbits = EXCEPTIONAL_A // 16
    generic_orbits = GENERIC_A // 16
    combined = generic_orbits * 36 + exceptional_orbits * 15
    assert all_orbits == 21_336
    assert exceptional_orbits == 35
    assert generic_orbits == 21_301
    assert combined == 767_361
    print('all_A_sets', ALL_A)
    print('generic_A_sets', GENERIC_A)
    print('exceptional_A_sets', EXCEPTIONAL_A)
    print('H210_A_orbits', all_orbits)
    print('generic_translation_orbits', generic_orbits)
    print('exceptional_translation_orbits', exceptional_orbits)
    print('H210_representatives', 768_096)
    print('H211_combined_representatives', combined)
    print('additional_saving', 768_096 - combined)


if __name__ == '__main__':
    main()
