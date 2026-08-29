"""Regression tests for lottery-only H inventory classification."""

from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "build_h_packet_inventory", ROOT / "tools/build_h_packet_inventory.py"
)
assert SPEC and SPEC.loader
inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory)


def test_explicit_terminal_success_negations_override_success_word() -> None:
    for statement in (
        "Status: PROMISING / NOT TERMINAL SUCCESS",
        "Status: NO TERMINAL SUCCESS",
        "Result\nTerminal SUCCESS: NOT ESTABLISHED",
        "Terminal SUCCESS: NOT PROVEN",
        "Status: NOT A SUCCESS",
        "State: CLOSED — NO SUCCESS",
    ):
        assert inventory.state(statement) != "SUCCESS"


def test_intermediate_success_is_not_terminal_success() -> None:
    text = """Status: OPEN
    Workflow completed successfully. Exact arithmetic test: SUCCESS.
    Terminal SUCCESS: NOT ESTABLISHED.
    """
    assert inventory.state(text) == "OPEN"


def test_success_requires_explicit_non_negated_terminal_statement() -> None:
    assert inventory.state("Terminal state: SUCCESS\nGuaranteed positive net profit proved.") == "SUCCESS"
    assert inventory.state("Terminal state: SUCCESS\nA workflow completed.") != "SUCCESS"
    assert inventory.state("Status: SUCCESSFUL VALIDATION") != "SUCCESS"


def test_known_false_success_packets_regression() -> None:
    for number in (137, 138, 164, 166, 167):
        files = [p for p in (ROOT / "research").iterdir() if f"h{number}" in p.name.lower()]
        source = inventory.best_markdown(files, number)
        assert source is not None
        assert inventory.state(source.read_text(encoding="utf-8")) != "SUCCESS"


def test_explicit_rejection_overrides_conditional_or_reopen_language() -> None:
    assert inventory.state(
        "Status: STRICT GUARANTEE REJECTED / CONDITIONAL OVERLAY PRESERVED"
    ) == "CLOSED"
    assert inventory.state(
        "Status: CURRENT EX-ANTE GUARANTEE REJECTED / CONDITIONAL STATE RETAINED"
    ) == "CLOSED"
    assert inventory.state(
        "Status: CLOSED under checked rules; candidate remains interesting if rules change"
    ) == "CLOSED"
    assert inventory.state(
        "Status: OPEN / candidate remains interesting\n\n## Result\nSTRICT GUARANTEE REJECTED under current rules."
    ) == "CLOSED"


def test_known_false_open_packets_regression() -> None:
    for number in (169, 170, 171, 182, 251, 252, 253):
        files = [p for p in (ROOT / "research").iterdir() if f"h{number}" in p.name.lower()]
        source = inventory.best_markdown(files, number)
        assert source is not None
        assert inventory.state(source.read_text(encoding="utf-8")) == "CLOSED"


def test_h225_exact_family_is_closed_exhausted() -> None:
    source = ROOT / "research/H225_EXACT_STATUS.md"
    assert inventory.status_number(source) == 225
    assert inventory.state(source.read_text(encoding="utf-8")) == "CLOSED / EXHAUSTED"


def test_non_lottery_drift_is_out_of_scope() -> None:
    assert inventory.is_lottery_packet(19)
    assert not inventory.is_lottery_packet(20)  # betting/market hedge packet
    assert not inventory.is_lottery_packet(56)  # bank/referral drift
    assert not inventory.is_lottery_packet(70)  # FX drift
    assert not inventory.is_lottery_packet(76)  # scrap drift
    assert not inventory.is_lottery_packet(92)  # claims drift
    assert inventory.is_lottery_packet(108)


def test_generated_inventory_has_no_false_success_or_drift() -> None:
    data = json.loads((ROOT / "data/derived/h_packet_inventory.json").read_text())
    packets = {packet["h_number"]: packet for packet in data["packets"]}
    assert data["scope"] == "LOTTERY ONLY"
    assert not ({20, *range(39, 108)} & packets.keys())
    assert not ({20, *range(39, 108)} & set(data["summary"]["intentional_or_unobserved_gaps"]))
    assert all(packet["state"] != "SUCCESS" for packet in packets.values())
    assert packets[225]["state"] == "CLOSED / EXHAUSTED"
    contradictory_open = [
        packet["h_number"]
        for packet in packets.values()
        if packet["state"] == "OPEN"
        and re.search(r"CLOS(?:URE|ED)|IMPOSSIB(?:ILITY|LE)|REJECT(?:ION|ED)|EXHAUSTED", packet["name"], re.I)
    ]
    assert contradictory_open == []
    assert data["summary"]["status_files_discovered"] == len(
        [
            path
            for path in (ROOT / "research").glob("H*_STATUS.md")
            if inventory.status_number(path) is not None
            and inventory.is_lottery_packet(inventory.status_number(path))
        ]
    )
