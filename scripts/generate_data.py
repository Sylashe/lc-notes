#!/usr/bin/env python3
"""Generate data.json from problems/ markdown files for the GitHub Pages dashboard."""

import json
import os
import re

PROBLEMS_DIR = os.path.join(os.path.dirname(__file__), "..", "problems")
OUT_FILE = os.path.join(os.path.dirname(__file__), "..", "docs", "data.json")


def parse_problem(path):
    fname = os.path.basename(path)
    # Derive slug from filename: "239-sliding-window-maximum.md" -> "sliding-window-maximum"
    slug_from_file = re.sub(r"^\d+-", "", fname[:-3])

    with open(path, encoding="utf-8") as f:
        content = f.read()

    number = re.search(r"^# (\d+)\.", content, re.MULTILINE)
    title = re.search(r"^# \d+\. (.+)$", content, re.MULTILINE)
    difficulty = re.search(r"\*\*Difficulty:\*\* (.+)", content)
    tags_line = re.search(r"\*\*Tags:\*\* (.+)", content)
    tags = re.findall(r"`([^`]+)`", tags_line.group(1) if tags_line else "")

    return {
        "id": int(number.group(1)) if number else 0,
        "title": title.group(1).strip() if title else "",
        "difficulty": difficulty.group(1).strip() if difficulty else "",
        "tags": tags,
        "slug": slug_from_file,
    }


def main():
    # Load timestamps
    ts_path = os.path.join(os.path.dirname(__file__), "..", "docs", "timestamps.json")
    timestamps = {}
    if os.path.exists(ts_path):
        with open(ts_path) as f:
            timestamps = json.load(f)

    problems = []
    for fname in os.listdir(PROBLEMS_DIR):
        if not fname.endswith(".md") or fname == "template.md":
            continue
        try:
            p = parse_problem(os.path.join(PROBLEMS_DIR, fname))
            if p["id"] > 0:
                p["ts"] = timestamps.get(p["slug"], 0)
                problems.append(p)
        except Exception as e:
            print(f"  Warning: {fname}: {e}")

    problems.sort(key=lambda x: x["id"])

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(problems, f, ensure_ascii=False)

    print(f"Generated {len(problems)} problems → docs/data.json")

    # Stats summary
    by_diff = {}
    by_tag = {}
    for p in problems:
        d = p["difficulty"] or "Unknown"
        by_diff[d] = by_diff.get(d, 0) + 1
        for t in p["tags"]:
            by_tag[t] = by_tag.get(t, 0) + 1

    print("Difficulty:", by_diff)
    top_tags = sorted(by_tag.items(), key=lambda x: -x[1])[:10]
    print("Top tags:", top_tags)


if __name__ == "__main__":
    main()
