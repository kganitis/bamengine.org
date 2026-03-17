#!/usr/bin/env python3
"""Generate SVG validation cards from the latest manifest data.

Reads static/data/validation/manifest.json and produces two SVG files:
  - static/images/validation-card-dark.svg  (GitHub dark mode)
  - static/images/validation-card-light.svg (GitHub light mode)

Each card shows three scenario sub-cards with accuracy, stability,
and color-coded status indicators.

Usage:
    python scripts/generate_validation_card.py
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
MANIFEST_PATH = ROOT / "static" / "data" / "validation" / "manifest.json"
CONFIG_PATH = ROOT / "data" / "validation_config.yaml"
OUTPUT_DIR = ROOT / "static" / "images"


def _load_config(path: Path) -> dict:
    """Minimal YAML loader for validation_config.yaml (stdlib only).

    Handles the single-level nesting used in our config: top-level scalars,
    one-deep mappings, and one-deep lists.  No PyYAML dependency required.
    """
    config: dict = {}
    section = None
    for line in path.read_text().splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if indent == 0:
            # Top-level key
            m = re.match(r"^(\w+):\s*(.*)", line)
            if not m:
                continue
            key, val = m.group(1), m.group(2).strip()
            if val:
                config[key] = val.strip('"')
            else:
                section = key
                config[section] = {}
        elif section is not None:
            # Nested item
            m_list = re.match(r"^\s+-\s+(.+)", line)
            m_kv = re.match(r"^\s+(\w+):\s+(.+)", line)
            if m_list:
                if not isinstance(config[section], list):
                    config[section] = []
                config[section].append(m_list.group(1).strip().strip('"'))
            elif m_kv:
                if isinstance(config[section], list):
                    config[section] = {}
                val = m_kv.group(2).strip().strip('"')
                try:
                    val = float(val)
                    if val == int(val):
                        val = int(val)
                except ValueError:
                    pass
                config[section][m_kv.group(1)] = val
    return config


_config = _load_config(CONFIG_PATH)
_thresholds = _config["thresholds"]

SCENARIOS = _config.get("scenario_order", ["baseline", "growth_plus", "buffer_stock"])
SCENARIO_NAMES = _config.get("scenario_names", {
    "baseline": "Baseline",
    "growth_plus": "Growth+",
    "buffer_stock": "Buffer-Stock",
})

# Thresholds (from data/validation_config.yaml)
PASS_GREEN = _thresholds["green_pass"] * 100  # pass_rate * 100
PASS_YELLOW = _thresholds["yellow_pass"] * 100
SCORE_GREEN = _thresholds["green_score"]
SCORE_YELLOW = _thresholds["yellow_score"]

# Theme colors
THEMES = {
    "dark": {
        "bg": "#161b22",
        "card_bg": "#0d1117",
        "border": "#30363d",
        "text": "#c9d1d9",
        "muted": "#8b949e",
        "green": "#3fb950",
        "yellow": "#d29922",
        "red": "#f85149",
    },
    "light": {
        "bg": "#ffffff",
        "card_bg": "#f6f8fa",
        "border": "#d0d7de",
        "text": "#1f2328",
        "muted": "#656d76",
        "green": "#1a7f37",
        "yellow": "#9a6700",
        "red": "#cf222e",
    },
}

FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

# Layout constants
CARD_W = 140
CARD_GAP = 12
PAD_X = 16
HEADER_H = 32


def _severity(pass_pct: float, score: float) -> int:
    """Return severity level: 2=green, 1=yellow, 0=red."""
    p = 2 if pass_pct >= PASS_GREEN else (1 if pass_pct >= PASS_YELLOW else 0)
    s = 2 if score >= SCORE_GREEN else (1 if score >= SCORE_YELLOW else 0)
    return min(p, s)


def _pass_color(pass_pct: float, theme: dict) -> str:
    if pass_pct >= PASS_GREEN:
        return theme["green"]
    if pass_pct >= PASS_YELLOW:
        return theme["yellow"]
    return theme["red"]


def _score_color(score: float, theme: dict) -> str:
    if score >= SCORE_GREEN:
        return theme["green"]
    if score >= SCORE_YELLOW:
        return theme["yellow"]
    return theme["red"]


def _dot_color(pass_pct: float, score: float, theme: dict) -> str:
    level = _severity(pass_pct, score)
    if level >= 2:
        return theme["green"]
    if level >= 1:
        return theme["yellow"]
    return theme["red"]


def _text(x: int, y: int, fill: str, size: int, text: str,
          weight: str = "400") -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" '
        f'font-weight="{weight}" font-family="{FONT}">{text}</text>'
    )


def generate_card(scenarios: dict, tag: str, theme_name: str) -> str:
    """Generate an SVG card string for the given theme."""
    theme = THEMES[theme_name]
    n = len(SCENARIOS)
    w = PAD_X * 2 + n * CARD_W + (n - 1) * CARD_GAP

    parts: list[str] = []

    # Header
    parts.append(_text(PAD_X, 21, theme["text"], 12, "Model Validation", "600"))
    if tag:
        parts.append(
            f'<text x="{w - PAD_X}" y="21" fill="{theme["muted"]}" '
            f'font-size="11" text-anchor="end" font-family="{FONT}">{tag}</text>'
        )
    parts.append(
        f'<line x1="0" y1="{HEADER_H}" x2="{w}" y2="{HEADER_H}" '
        f'stroke="{theme["border"]}"/>'
    )

    max_card_h = 0

    for i, key in enumerate(SCENARIOS):
        info = scenarios.get(key)
        if info is None:
            continue

        pass_pct = info["pass_rate"] * 100
        score = info["mean_score"]
        name = SCENARIO_NAMES[key]

        cx = PAD_X + i * (CARD_W + CARD_GAP)
        cy = HEADER_H + 12
        dot_c = _dot_color(pass_pct, score, theme)
        score_c = _score_color(score, theme)
        pass_c = _pass_color(pass_pct, theme)

        card_parts: list[str] = []

        # Status dot + scenario name
        card_parts.append(
            f'<circle cx="{cx + 10}" cy="{cy + 12}" r="4" fill="{dot_c}"/>'
        )
        card_parts.append(
            _text(cx + 19, cy + 16, theme["text"], 11, name, "600")
        )

        inner_y = 24

        # Mean score (large, color-coded)
        inner_y += 20
        card_parts.append(
            _text(cx + 10, cy + inner_y, score_c, 20, f"{score:.3f}", "700")
        )
        inner_y += 14
        card_parts.append(
            _text(cx + 10, cy + inner_y, theme["muted"], 10, "accuracy")
        )

        # Pass rate (smaller, color-coded)
        inner_y += 18
        card_parts.append(
            _text(cx + 10, cy + inner_y, pass_c, 14, f"{pass_pct:.1f}%", "600")
        )
        inner_y += 14
        card_parts.append(
            _text(cx + 10, cy + inner_y, theme["muted"], 10, "stability")
        )

        card_h = inner_y + 12
        if card_h > max_card_h:
            max_card_h = card_h

        # Card background (rendered before content)
        parts.append(
            f'<rect x="{cx}" y="{cy}" width="{CARD_W}" height="{card_h}" '
            f'rx="4" fill="{theme["card_bg"]}" stroke="{theme["border"]}"/>'
        )
        parts.extend(card_parts)

    h = HEADER_H + 12 + max_card_h + 12

    content = "\n  ".join(parts)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}">\n'
        f'  <rect width="{w}" height="{h}" rx="6" fill="{theme["bg"]}" '
        f'stroke="{theme["border"]}"/>\n'
        f'  {content}\n'
        f'</svg>\n'
    )


def main() -> None:
    if not MANIFEST_PATH.exists():
        print("No manifest.json found — skipping card generation")
        return

    manifest = json.loads(MANIFEST_PATH.read_text())
    runs = manifest.get("runs", [])
    if not runs:
        print("Manifest has no runs — skipping card generation")
        return

    latest = runs[0]
    scenarios = latest["scenarios"]
    tag = latest.get("tag") or ""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for theme_name in ("dark", "light"):
        svg = generate_card(scenarios, tag, theme_name)
        out_path = OUTPUT_DIR / f"validation-card-{theme_name}.svg"
        out_path.write_text(svg)
        print(f"Generated {out_path.name}")


if __name__ == "__main__":
    main()