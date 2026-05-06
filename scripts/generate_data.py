#!/usr/bin/env python3
"""Generate data.json from problems/ markdown files for the GitHub Pages dashboard."""

import json
import os
import re

PROBLEMS_DIR = os.path.join(os.path.dirname(__file__), "..", "problems")
OUT_FILE = os.path.join(os.path.dirname(__file__), "..", "docs", "data.json")


def parse_problem(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    number = re.search(r"^# (\d+)\.", content, re.MULTILINE)
    title = re.search(r"^# \d+\. (.+)$", content, re.MULTILINE)
    difficulty = re.search(r"\*\*Difficulty:\*\* (.+)", content)
    tags = re.findall(r"`([^`]+)`", (re.search(r"\*\*Tags:\*\* (.+)", content) or type('', (), {'group': lambda s, x: ''})()).group(1) if re.search(r"\*\*Tags:\*\* (.+)", content) else "")
    slug = re.search(r"https://leetcode\.com/problems/([^/]+)/", content)

    return {
        "id": int(number.group(1)) if number else 0,
        "title": title.group(1).strip() if title else "",
        "difficulty": difficulty.group(1).strip() if difficulty else "",
        "tags": tags,
        "slug": slug.group(1) if slug else "",
    }


def main():
    problems = []
    for fname in os.listdir(PROBLEMS_DIR):
        if not fname.endswith(".md") or fname == "template.md":
            continue
        try:
            p = parse_problem(os.path.join(PROBLEMS_DIR, fname))
            if p["id"] > 0:
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
