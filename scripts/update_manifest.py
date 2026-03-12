#!/usr/bin/env python3
"""Regenerate data/stability/manifest.json from result JSON files.

Scans data/stability/*.json (excluding manifest.json), groups by commit,
deduplicates (latest timestamp wins per scenario+commit), and writes a
sorted manifest with inlined summary stats.

Usage:
    python scripts/update_manifest.py
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data" / "stability"
MANIFEST_PATH = DATA_DIR / "manifest.json"


def main() -> None:
    # Scan all JSON files except the manifest itself
    result_files = sorted(DATA_DIR.glob("*.json"))
    result_files = [f for f in result_files if f.name != "manifest.json"]

    if not result_files:
        print("No result files found in data/stability/")
        MANIFEST_PATH.write_text(json.dumps({"runs": []}, indent=2) + "\n")
        print(f"Wrote empty manifest to {MANIFEST_PATH}")
        return

    # Parse files and group by commit
    # Key: commit_full -> {timestamp, tag, scenarios: {scenario -> (file, summary)}}
    commits: dict[str, dict] = {}

    for filepath in result_files:
        try:
            data = json.loads(filepath.read_text())
        except (json.JSONDecodeError, KeyError) as e:
            print(f"WARNING: Skipping {filepath.name}: {e}")
            continue

        meta = data.get("metadata", {})
        commit_full = meta.get("commit", "")
        commit_short = meta.get("commit_short", "")
        timestamp = meta.get("timestamp", "")
        tag = meta.get("tag")
        scenario = data.get("scenario", "")
        summary = data.get("summary", {})

        if not commit_full or not scenario:
            print(f"WARNING: Skipping {filepath.name}: missing commit or scenario")
            continue

        if commit_full not in commits:
            commits[commit_full] = {
                "commit_short": commit_short,
                "commit": commit_full,
                "timestamp": timestamp,
                "tag": tag,
                "scenarios": {},
            }

        # Deduplication: latest timestamp wins per scenario+commit
        existing = commits[commit_full]["scenarios"].get(scenario)
        if existing is None or timestamp > existing.get("_timestamp", ""):
            commits[commit_full]["scenarios"][scenario] = {
                "file": filepath.name,
                "pass_rate": summary.get("pass_rate", 0),
                "mean_score": summary.get("mean_score", 0),
                "_timestamp": timestamp,  # internal, stripped before output
            }

        # Update commit-level timestamp to latest
        if timestamp > commits[commit_full]["timestamp"]:
            commits[commit_full]["timestamp"] = timestamp

    # Build manifest
    runs = []
    for commit_data in commits.values():
        # Strip internal _timestamp from scenarios
        scenarios = {}
        for name, info in commit_data["scenarios"].items():
            scenarios[name] = {
                "file": info["file"],
                "pass_rate": info["pass_rate"],
                "mean_score": info["mean_score"],
            }

        runs.append({
            "commit_short": commit_data["commit_short"],
            "commit": commit_data["commit"],
            "timestamp": commit_data["timestamp"],
            "tag": commit_data["tag"],
            "scenarios": scenarios,
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


if __name__ == "__main__":
    main()