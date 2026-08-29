#!/usr/bin/env python3
"""Build the current, lottery-only inventory of numbered H research packets.

Discovery is filename-based across research/, src/, data/, and tests/.  The explicit
scope boundary excludes the old non-lottery drift without deleting its files. Status
and terminal statements are authoritative when present; otherwise the most
descriptive Markdown report is used. Intentional number gaps remain gaps.
"""
from __future__ import annotations
import json, re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = ("research", "src", "data", "tests")
PACKET_RE = re.compile(r"(?i)(?:^|[_-])h(\d{1,3})(?:[_\-.]|$)")
STATUS_RE = re.compile(r"(?i)^H(\d{1,3})_STATUS\.md$")
EXACT_STATUS_RE = re.compile(r"(?i)^H(225)_EXACT_STATUS\.md$")
RATIO_RE = re.compile(r"(?i)(?:return|ratio|gross|floor)[^\n%]{0,70}?([0-9]+(?:\.[0-9]+)?)\s*%")

# Repository history temporarily drifted from lottery research after H019, with
# H020 and H039-H107 covering betting, banking, FX, scrap, claims, and similar
# mechanisms. Lottery research resumes at H108. Keeping this boundary explicit is
# safer and auditable; semantic keyword guessing would silently leak drift back in.
NON_LOTTERY_PACKET_NUMBERS = frozenset({20, *range(39, 108)})


def is_lottery_packet(number: int) -> bool:
    """Return whether an H number belongs to the current lottery packet map."""
    return number not in NON_LOTTERY_PACKET_NUMBERS


def status_number(path: Path) -> int | None:
    """Map both ordinary and the authoritative H225 exact status to a packet."""
    match = STATUS_RE.match(path.name) or EXACT_STATUS_RE.match(path.name)
    return int(match.group(1)) if match else None


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            value = re.sub(r"^#\s*H\d+\s*(?:STATUS)?\s*[-—:]?\s*", "", line, flags=re.I).strip()
            if value and value.upper() != "STATUS":
                return value
    return fallback


def state(text: str) -> str:
    """Classify terminal state conservatively from authoritative statements.

    SUCCESS is deliberately fail-closed: an isolated word, a successful workflow,
    or a validated intermediate theorem can never produce it. The document must
    explicitly establish terminal project success and must contain no explicit
    terminal-success negation.
    """
    upper = text.upper()
    authoritative = "\n".join(
        line for line in upper.splitlines()
        if re.match(r"^\s*(?:UPDATED\s+)?(?:STATUS|STATE|TERMINAL\s+STATE|TERMINAL\s+SUCCESS)\s*:", line.replace("*", ""))
    )
    sample = authoritative or upper[:2500]
    negative_success = bool(re.search(
        r"(?:NO|NOT)\s+(?:CURRENT\s+|TERMINAL\s+)?SUCCESS|"
        r"TERMINAL\s+SUCCESS\s*:\s*(?:NO|NOT|UNPROVEN|NOT\s+ESTABLISHED)|"
        r"SUCCESS\s*:\s*(?:NO|NOT)",
        upper,
    ))
    terminal_success = bool(re.search(
        r"TERMINAL\s+(?:STATE|SUCCESS)\s*:\s*(?:SUCCESS|ESTABLISHED|PROVEN)",
        authoritative,
    ))
    success_proof = bool(re.search(
        r"(?:GUARANTEED|STRICT(?:LY)?\s+PROVEN)[^\n.]{0,100}POSITIVE[^\n.]{0,50}"
        r"(?:NET\s+)?(?:PROFIT|CASH\s+FLOOR)|"
        r"POSITIVE\s+NET\s+PROFIT[^\n.]{0,100}(?:EVERY|ALL)\s+(?:LEGAL|REQUIRED)",
        upper,
    ))
    if terminal_success and success_proof and not negative_success:
        return "SUCCESS"
    if "CLOSED" in sample and "EXHAUSTED" in sample:
        return "CLOSED / EXHAUSTED"
    if "EXHAUSTED" in sample:
        return "EXHAUSTED"
    if any(x in sample for x in ("EVIDENCE-BLOCKED", "DATA-BLOCKED", "EVIDENCE BLOCKED")):
        return "EVIDENCE-BLOCKED"
    if any(x in sample for x in ("OPEN", "PROMISING", "CONDITIONAL", "INCONCLUSIVE", "REMAINS")) and "CLOSED" not in sample:
        return "OPEN"
    if any(x in sample for x in ("CLOSED", "REJECTED", "COMPLETE")) or negative_success:
        return "CLOSED"
    return "UNCLASSIFIED"


def paragraph_after(text: str, labels: tuple[str, ...]) -> str | None:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if any(label in line.upper() for label in labels):
            parts=[]
            for nxt in lines[i+1:i+12]:
                if nxt.startswith("#") and parts: break
                if nxt.strip(): parts.append(nxt.strip(" -*"))
                elif parts: break
            if parts:
                return " ".join(parts)[:600]
    return None


def best_markdown(files: list[Path], n: int) -> Path | None:
    status = [p for p in files if status_number(p) == n]
    if status: return sorted(status)[0]
    md = [p for p in files if p.suffix.lower()==".md" and "APPEND" not in p.name.upper() and "VALIDATION" not in p.name.upper()]
    if not md: return None
    def rank(p: Path) -> tuple[int,int,str]:
        name=p.name.lower()
        return (0 if name.startswith(f"h{n}_") else 1, len(name), name)
    return sorted(md,key=rank)[0]


def main() -> None:
    grouped: dict[int, list[Path]] = defaultdict(list)
    for directory in SCAN_DIRS:
        base=ROOT/directory
        if not base.exists(): continue
        for p in base.rglob("*"):
            if not p.is_file(): continue
            m=PACKET_RE.search(p.name)
            if m and is_lottery_packet(int(m.group(1))):
                grouped[int(m.group(1))].append(p)

    packets=[]; unparsed=[]; duplicate_status=[]
    all_status=[p for p in (ROOT/"research").glob("H*_STATUS.md")
                if (status_number(p) is not None and is_lottery_packet(status_number(p)))]
    for n in sorted(grouped):
        files=sorted(set(grouped[n]), key=rel)
        statuses=[p for p in files if status_number(p) == n]
        if len(statuses)>1: duplicate_status.append({"h_number":n,"files":[rel(p) for p in statuses]})
        source=best_markdown(files,n)
        if source is None:
            unparsed.append({"h_number":n,"reason":"no Markdown report/status","files":[rel(p) for p in files]})
            continue
        text=source.read_text(encoding="utf-8",errors="replace")
        ratios=[float(x) for x in RATIO_RE.findall(text)]
        result=paragraph_after(text,("## RESULT","## COMPLETED CHECKPOINT","## STRICT GUARANTEE BLOCKER"))
        reopen=paragraph_after(text,("## NEXT ACTION","REOPEN ONLY","REOPENING CONDITION"))
        packets.append({
            "h_number":n,
            "name":heading(text, source.stem),
            "state":state(text),
            "main_result_or_blocker":result or "See key files; older packet lacks a standardized result section.",
            "best_reported_ratio_percent":max(ratios) if ratios else None,
            "key_files":[rel(p) for p in files if p.suffix.lower() in {".md",".py",".json"}][:12],
            "reopening_condition":reopen or "No explicit reopening condition recorded; require materially new rules or evidence.",
            "inventory_source":rel(source),
        })

    status_numbers={status_number(p) for p in all_status}
    represented={p["h_number"] for p in packets}
    unrepresented_status=sorted(status_numbers-represented)
    gaps=[n for n in range(min(grouped),max(grouped)+1)
          if is_lottery_packet(n) and n not in grouped]
    summary={
        "discovered_packet_numbers":len(grouped), "parsed_packets":len(packets),
        "skipped_or_unparsed":len(unparsed), "status_files_discovered":len(all_status),
        "status_files_unrepresented":unrepresented_status,
        "duplicate_status_conflicts":duplicate_status,
        "intentional_or_unobserved_gaps":gaps,
    }
    out={"generated_by":"tools/build_h_packet_inventory.py","scope":"LOTTERY ONLY",
         "excluded_non_lottery_packet_numbers":sorted(NON_LOTTERY_PACKET_NUMBERS),
         "summary":summary,"packets":packets,"unparsed":unparsed}
    outpath=ROOT/"data/derived/h_packet_inventory.json"
    outpath.parent.mkdir(parents=True,exist_ok=True)
    outpath.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    lines=["# H Packet Index — Lottery Only","", "Generated reproducibly by `tools/build_h_packet_inventory.py` from lottery packet evidence in the repository.",
           "Old non-lottery drift (H020 and H039-H107: betting, banking, FX, scrap, claims, and related work) remains in the repository but is intentionally excluded from this current navigation map.","",
           "## Validation counts","",
           f"- Discovered packet numbers: **{summary['discovered_packet_numbers']}**.",
           f"- Parsed records: **{summary['parsed_packets']}**.",
           f"- Skipped/unparsed: **{summary['skipped_or_unparsed']}**.",
           f"- In-scope authoritative status files (`H*_STATUS.md`, including `H225_EXACT_STATUS.md`): **{summary['status_files_discovered']}**; unrepresented: **{len(unrepresented_status)}**.",
           f"- Duplicate status conflicts: **{len(duplicate_status)}**.",
           f"- Filename gaps (not invented as research): **{', '.join('H'+str(x) for x in gaps) if gaps else 'none'}**.","",
           "The JSON record is authoritative for full file lists and extracted blocker/reopening text. `SUCCESS` is reserved for an explicit, non-negated terminal project success; successful intermediate tests never qualify. `UNCLASSIFIED` does not imply an open lead.","",
           "## Inventory","", "| H | State | Packet / mechanism | Best reported ratio | Inventory source |", "|---:|---|---|---:|---|"]
    for p in packets:
        ratio="—" if p["best_reported_ratio_percent"] is None else f"{p['best_reported_ratio_percent']:.6g}%"
        name=p["name"].replace("|","\\|")[:105]
        lines.append(f"| H{p['h_number']} | {p['state']} | {name} | {ratio} | `{p['inventory_source']}` |")
    (ROOT/"research/H_PACKET_INDEX.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(f"discovered={len(grouped)} parsed={len(packets)} skipped={len(unparsed)} duplicate_conflicts={len(duplicate_status)} status_unrepresented={len(unrepresented_status)}")
    if unrepresented_status or duplicate_status: raise SystemExit(1)

if __name__ == "__main__": main()
