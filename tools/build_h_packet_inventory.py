#!/usr/bin/env python3
"""Build a reproducible inventory of numbered H research packets.

Discovery is filename-based across research/, src/, data/, and tests/.  Status files
are authoritative when present; otherwise the most descriptive Markdown report is
used. Intentional number gaps remain gaps. No packet is inferred from a number alone.
"""
from __future__ import annotations
import json, re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = ("research", "src", "data", "tests")
PACKET_RE = re.compile(r"(?i)(?:^|[_-])h(\d{1,3})(?:[_\-.]|$)")
STATUS_RE = re.compile(r"(?i)^H(\d{1,3})_STATUS\.md$")
RATIO_RE = re.compile(r"(?i)(?:return|ratio|gross|floor)[^\n%]{0,70}?([0-9]+(?:\.[0-9]+)?)\s*%")


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
    upper = text.upper()
    state_lines = "\n".join(line for line in upper.splitlines()[:35] if "STATE" in line or "STATUS" in line)
    sample = state_lines or upper[:2500]
    if "SUCCESS" in sample and not any(x in sample for x in ("NOT SUCCESS", "NO SUCCESS", "SUCCESS: NO")):
        return "SUCCESS"
    if "EXHAUSTED" in sample and "H225" not in sample[:400]:
        return "EXHAUSTED"
    if any(x in sample for x in ("EVIDENCE-BLOCKED", "DATA-BLOCKED", "EVIDENCE BLOCKED")):
        return "EVIDENCE-BLOCKED"
    if any(x in sample for x in ("OPEN", "PROMISING", "INCONCLUSIVE")) and "CLOSED" not in sample:
        return "OPEN"
    if any(x in sample for x in ("CLOSED", "REJECTED", "NOT SUCCESS", "NO SUCCESS", "COMPLETE")):
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
    status = [p for p in files if STATUS_RE.match(p.name)]
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
            if m: grouped[int(m.group(1))].append(p)

    packets=[]; unparsed=[]; duplicate_status=[]
    all_status=list((ROOT/"research").glob("H*_STATUS.md"))
    for n in sorted(grouped):
        files=sorted(set(grouped[n]), key=rel)
        statuses=[p for p in files if STATUS_RE.match(p.name)]
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

    status_numbers={int(STATUS_RE.match(p.name).group(1)) for p in all_status if STATUS_RE.match(p.name)}
    represented={p["h_number"] for p in packets}
    unrepresented_status=sorted(status_numbers-represented)
    gaps=[n for n in range(min(grouped),max(grouped)+1) if n not in grouped]
    summary={
        "discovered_packet_numbers":len(grouped), "parsed_packets":len(packets),
        "skipped_or_unparsed":len(unparsed), "status_files_discovered":len(all_status),
        "status_files_unrepresented":unrepresented_status,
        "duplicate_status_conflicts":duplicate_status,
        "intentional_or_unobserved_gaps":gaps,
    }
    out={"generated_by":"tools/build_h_packet_inventory.py","summary":summary,"packets":packets,"unparsed":unparsed}
    outpath=ROOT/"data/derived/h_packet_inventory.json"
    outpath.parent.mkdir(parents=True,exist_ok=True)
    outpath.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    lines=["# H Packet Index","", "Generated reproducibly by `tools/build_h_packet_inventory.py` from packet evidence in the repository.","",
           "## Validation counts","",
           f"- Discovered packet numbers: **{summary['discovered_packet_numbers']}**.",
           f"- Parsed records: **{summary['parsed_packets']}**.",
           f"- Skipped/unparsed: **{summary['skipped_or_unparsed']}**.",
           f"- Discovered `H*_STATUS.md` files: **{summary['status_files_discovered']}**; unrepresented: **{len(unrepresented_status)}**.",
           f"- Duplicate status conflicts: **{len(duplicate_status)}**.",
           f"- Filename gaps (not invented as research): **{', '.join('H'+str(x) for x in gaps) if gaps else 'none'}**.","",
           "The JSON record is authoritative for full file lists and extracted blocker/reopening text. `UNCLASSIFIED` means older evidence did not use a standardized state label; it does not imply an open lead.","",
           "## Inventory","", "| H | State | Packet / mechanism | Best reported ratio | Inventory source |", "|---:|---|---|---:|---|"]
    for p in packets:
        ratio="—" if p["best_reported_ratio_percent"] is None else f"{p['best_reported_ratio_percent']:.6g}%"
        name=p["name"].replace("|","\\|")[:105]
        lines.append(f"| H{p['h_number']} | {p['state']} | {name} | {ratio} | `{p['inventory_source']}` |")
    (ROOT/"research/H_PACKET_INDEX.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(f"discovered={len(grouped)} parsed={len(packets)} skipped={len(unparsed)} duplicate_conflicts={len(duplicate_status)} status_unrepresented={len(unrepresented_status)}")
    if unrepresented_status or duplicate_status: raise SystemExit(1)

if __name__ == "__main__": main()
