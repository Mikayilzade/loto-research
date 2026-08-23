"""H233: deterministic repair gate for the corrupted H185 witness bank.

This is intentionally conservative: a candidate repair is accepted only if it
recovers the documented H185 object exactly enough to satisfy all structural
invariants available in the repository.
"""
from __future__ import annotations

import base64
import json
import zlib
from pathlib import Path

from loto_research.h185_h180_affine_orbit_cut_acceleration import active_rows

ROOT = Path(__file__).resolve().parents[2]
DERIVED = ROOT / "data" / "derived"
TARGET = DERIVED / "h185_h180_witness_bank.zlib.b64"
BASE = DERIVED / "h183_h180_witness_bank.zlib.b64"
H184 = DERIVED / "h184_h183_new_witnesses.json"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def _clean(path: Path) -> str:
    return "".join(path.read_text().split()).rstrip("=")


def _decode_text(s: str):
    s = s + "=" * (-len(s) % 4)
    raw = base64.b64decode(s, validate=True)
    return json.loads(zlib.decompress(raw))


def _reference():
    base = _decode_text(_clean(BASE))
    if len(base) != 254:
        raise RuntimeError(f"H183 reference count changed: {len(base)}")
    h184 = json.loads(H184.read_text())["witnesses"]
    if len(h184) != 1:
        raise RuntimeError(f"H184 delta count changed: {len(h184)}")
    return base, h184[0]


def _valid(bank, base, h184_witness) -> bool:
    if not isinstance(bank, list) or len(bank) != 297:
        return False
    if bank[:254] != base or bank[254] != h184_witness:
        return False
    for w in bank:
        if not isinstance(w, list) or len(w) != 5:
            return False
        for g in w:
            if not isinstance(g, list) or len(g) != 4:
                return False
            if len(set(g)) != 4 or any(not isinstance(x, int) or x < 0 or x >= 16 for x in g):
                return False
    return len(active_rows(bank)) == 4878


def _try(s: str, base, h184_witness):
    try:
        bank = _decode_text(s)
    except (ValueError, zlib.error, json.JSONDecodeError, UnicodeDecodeError):
        return None
    return bank if _valid(bank, base, h184_witness) else None


def _single_substitution(s: str, base, h184_witness):
    for i, old in enumerate(s):
        if old not in ALPHABET:
            continue
        for ch in ALPHABET:
            if ch == old:
                continue
            bank = _try(s[:i] + ch + s[i + 1 :], base, h184_witness)
            if bank is not None:
                return bank, f"single_base64_substitution index={i} {old}->{ch}"
    return None


def _single_deletion(s: str, base, h184_witness):
    for i in range(len(s)):
        bank = _try(s[:i] + s[i + 1 :], base, h184_witness)
        if bank is not None:
            return bank, f"single_extra_base64_character index={i} char={s[i]}"
    return None


def _single_insertion(s: str, base, h184_witness):
    for i in range(len(s) + 1):
        for ch in ALPHABET:
            bank = _try(s[:i] + ch + s[i:], base, h184_witness)
            if bank is not None:
                return bank, f"single_missing_base64_character index={i} char={ch}"
    return None


def main():
    base, h184_witness = _reference()
    damaged = _clean(TARGET)

    bank = _try(damaged, base, h184_witness)
    repair = "none"
    if bank is None:
        found = _single_substitution(damaged, base, h184_witness)
        if found is None:
            found = _single_deletion(damaged, base, h184_witness)
        if found is None:
            found = _single_insertion(damaged, base, h184_witness)
        if found is None:
            raise RuntimeError("H233 could not recover H185 with a single local Base64 edit")
        bank, repair = found

    payload = json.dumps(bank, separators=(",", ":")).encode()
    encoded = base64.b64encode(zlib.compress(payload, 9)).decode() + "\n"
    TARGET.write_text(encoded)

    # Re-read the exact file we wrote before reporting success.
    check = _decode_text(_clean(TARGET))
    if not _valid(check, base, h184_witness):
        raise RuntimeError("H233 post-write validation failed")

    print("repair", repair)
    print("stored_witnesses", len(check))
    print("active_unique_rows", len(active_rows(check)))
    print("H233_REPAIR_VALIDATED")


if __name__ == "__main__":
    main()

# Push after workflow installation so H233 is guaranteed to receive a push event.
