#!/usr/bin/env python3
"""Regenerate data/validation/manifest.json from result JSON files.

Scans data/validation/*.json (excluding manifest.json), groups by commit,
deduplicates (latest timestamp wins per scenario+commit), and writes a
sorted manifest with inlined summary stats.

Usage:
    python scripts/update_manifest.py
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "static" / "data" / "validation"
MANIFEST_PATH = DATA_DIR / "manifest.json"


def main() -> None:
    # Scan all JSON files except the manifest itself
    result_files = sorted(DATA_DIR.glob("*.json"))
    result_files = [f for f in result_files if f.name != "manifest.json"]

    if not result_files:
        print("No result files found in data/validation/")
        MANIFEST_PATH.write_text(json.dumps({"runs": []}, indent=2) + "\n")
        print(f"Wrote empty manifest to {MANIFEST_PATH}")
        return

    # Parse files and group by commit
    # Key: commit_full -> {timestamp, tag, scenarios: {scenario -> {file, pass_rate, mean_score}}}
    commits: dict[str, dict] = {}
    # Track latest timestamp per scenario+commit for deduplication
    scenario_timestamps: dict[tuple[str, str], str] = {}

    for filepath in result_files:
        try:
            data = json.loads(filepath.read_text())
        except (json.JSONDecodeError, OSError) as e:
            print(f"WARNING: Skipping {filepath.name}: {e}")
            continue

        meta = data.get("metadata", {})
        commit_full = meta.get("commit", "")
        commit_short = meta.get("commit_short", "") or commit_full[:7]
        timestamp = meta.get("timestamp", "")
        tag = meta.get("tag")
        scenario = data.get("scenario", "")
        summary = data.get("summary", {})

        if not commit_full or not scenario:
            print(f"WARNING: Skipping {filepath.name}: missing commit or scenario")
            continue

        commit_date = meta.get("commit_date")

        if commit_full not in commits:
            commits[commit_full] = {
                "commit_short": commit_short,
                "commit": commit_full,
                "commit_date": commit_date,
                "timestamp": timestamp,
                "tag": tag,
                "scenarios": {},
            }

        # Deduplication: latest timestamp wins per scenario+commit
        dedup_key = (commit_full, scenario)
        prev_ts = scenario_timestamps.get(dedup_key, "")
        if timestamp > prev_ts:
            scenario_timestamps[dedup_key] = timestamp
            failing_seeds = data.get("failing_seeds", [])
            commits[commit_full]["scenarios"][scenario] = {
                "file": filepath.name,
                "pass_rate": summary.get("pass_rate", 0),
                "mean_score": summary.get("mean_score", 0),
                "n_failing": len(failing_seeds),
            }

        # Update commit-level fields when better values are available
        if timestamp > commits[commit_full]["timestamp"]:
            commits[commit_full]["timestamp"] = timestamp
        if commits[commit_full]["tag"] is None and tag is not None:
            commits[commit_full]["tag"] = tag
        if commits[commit_full]["commit_date"] is None and commit_date is not None:
            commits[commit_full]["commit_date"] = commit_date

    # Build manifest
    runs = []
    for commit_data in commits.values():
        runs.append({
            "commit_short": commit_data["commit_short"],
            "commit": commit_data["commit"],
            "commit_date": commit_data["commit_date"],
            "timestamp": commit_data["timestamp"],
            "tag": commit_data["tag"],
            "scenarios": commit_data["scenarios"],
        })

    # Sort by timestamp (newest first)
    runs.sort(key=lambda r: r["timestamp"], reverse=True)

    manifest = {"runs": runs}
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"Manifest updated: {len(runs)} commits, {sum(len(r['scenarios']) for r in runs)} scenario results")
    for run in runs[:5]:
        tag_str = f" ({run['tag']})" if run.get("tag") else ""
        scenarios_str = ", ".join(
            f"{s}: {info['pass_rate']:.1%}"
            for s, info in run["scenarios"].items()
        )
        print(f"  {run['commit_short']}{tag_str}: {scenarios_str}")
    if len(runs) > 5:
        print(f"  ... and {len(runs) - 5} more")

    # Regenerate validation card SVGs
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from generate_validation_card import main as generate_cards
    generate_cards()


if __name__ == "__main__":
    main()
