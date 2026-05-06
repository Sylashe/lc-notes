#!/usr/bin/env python3
"""
Fetch LeetCode accepted submissions and generate problem notes.
Usage: python scripts/fetch_leetcode.py --cookie "your_session_cookie"
"""

import argparse
import json
import os
import re
import time
import requests

USERNAME = "ieFnaHeH"
PROBLEMS_DIR = os.path.join(os.path.dirname(__file__), "..", "problems")

GRAPHQL_URL = "https://leetcode.com/graphql"

HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "User-Agent": "Mozilla/5.0",
}

LANG_EXT = {
    "python": "py", "python3": "py", "java": "java", "cpp": "cpp",
    "c": "c", "javascript": "js", "typescript": "ts", "go": "go",
    "rust": "rs", "kotlin": "kt", "swift": "swift", "ruby": "rb",
    "scala": "scala", "csharp": "cs",
}

LANG_FENCE = {
    "python": "python", "python3": "python", "java": "java", "cpp": "cpp",
    "c": "c", "javascript": "javascript", "typescript": "typescript",
    "go": "go", "rust": "rust", "kotlin": "kotlin", "swift": "swift",
}


def gql(session, query, variables=None, retries=3):
    for attempt in range(retries):
        resp = session.post(GRAPHQL_URL, json={"query": query, "variables": variables or {}})
        if resp.ok:
            return resp.json()
        if resp.status_code in (429, 503, 504) and attempt < retries - 1:
            wait = (attempt + 1) * 5
            print(f"\n  HTTP {resp.status_code}, retrying in {wait}s...")
            time.sleep(wait)
            continue
        if resp.status_code == 404:
            return {}  # silently skip inaccessible submissions
        print(f"\n  HTTP {resp.status_code}: {resp.text[:300]}")
        resp.raise_for_status()
    return {}


def fetch_all_solved_problems(session):
    """Return all problems the user has interacted with, paginated via userProgressQuestionList."""
    query = """
    query userProgressQuestionList($filters: UserProgressQuestionListInput!) {
      userProgressQuestionList(filters: $filters) {
        totalNum
        questions {
          questionFrontendId
          title
          titleSlug
          difficulty
          lastResult
          topicTags { name }
        }
      }
    }
    """
    limit = 50
    skip = 0
    all_questions = []

    while True:
        # Build inline query to avoid GraphQL variable type issues with nested filters
        inline_query = f"""
        query {{
          userProgressQuestionList(filters: {{limit: {limit}, skip: {skip}}}) {{
            totalNum
            questions {{
              frontendId
              title
              titleSlug
              difficulty
              lastResult
              topicTags {{ name }}
            }}
          }}
        }}
        """
        data = gql(session, inline_query)
        result = (data.get("data") or {}).get("userProgressQuestionList") or {}
        questions = result.get("questions") or []
        total = result.get("totalNum", 0)

        if not questions:
            break

        ac = [q for q in questions if q.get("lastResult") == "AC"]
        all_questions.extend(ac)
        skip += len(questions)
        print(f"  Fetched {skip}/{total}, {len(all_questions)} AC so far...")

        if skip >= total:
            break
        time.sleep(0.3)

    print(f"  Total AC problems: {len(all_questions)}")
    return all_questions


def fetch_latest_ac_submission(session, slug):
    """Get the latest AC submission id and lang for a problem."""
    query = """
    query submissionList($offset: Int!, $limit: Int!, $questionSlug: String!) {
      submissionList(offset: $offset, limit: $limit, questionSlug: $questionSlug) {
        submissions {
          id
          lang
          statusDisplay
        }
      }
    }
    """
    data = gql(session, query, {"offset": 0, "limit": 10, "questionSlug": slug})
    subs = ((data.get("data") or {}).get("submissionList") or {}).get("submissions") or []
    for sub in subs:
        if sub.get("statusDisplay") == "Accepted":
            return sub["id"], sub["lang"]
    return None, None


def fetch_submission_code(session, submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
        lang { name verboseName }
      }
    }
    """
    data = gql(session, query, {"submissionId": int(submission_id)})
    details = (data.get("data") or {}).get("submissionDetails") or {}
    return details.get("code", ""), (details.get("lang") or {}).get("name", "python3")


def fetch_problem_detail(session, slug):
    query = """
    query questionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        difficulty
        topicTags { name slug }
        content
      }
    }
    """
    data = gql(session, query, {"titleSlug": slug})
    return (data.get("data") or {}).get("question") or {}


def strip_html(html):
    """Very lightweight HTML stripper for problem descriptions."""
    text = re.sub(r"<[^>]+>", "", html or "")
    text = text.replace("&nbsp;", " ").replace("&lt;", "<").replace("&gt;", ">") \
               .replace("&amp;", "&").replace("&quot;", '"').replace("&#39;", "'")
    return text.strip()


def safe_filename(number, title):
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return f"{number}-{slug}.md"


def note_exists(number, title):
    fname = safe_filename(number, title)
    return os.path.exists(os.path.join(PROBLEMS_DIR, fname))


def write_note(problem, code, lang):
    number = problem.get("questionFrontendId", "?")
    title = problem.get("title", "Unknown")
    difficulty = problem.get("difficulty", "")
    tags = [t["name"] for t in (problem.get("topicTags") or [])]
    slug = problem.get("titleSlug", "")

    description_html = problem.get("content") or ""
    description = strip_html(description_html)
    # Keep only first ~400 chars as summary
    summary = description[:400].replace("\n", " ").strip()
    if len(description) > 400:
        summary += "..."

    fence = LANG_FENCE.get(lang, lang)
    tag_str = " ".join(f"`{t}`" for t in tags) if tags else ""

    note = f"""# {number}. {title}

**Link:** https://leetcode.com/problems/{slug}/
**Difficulty:** {difficulty}
**Tags:** {tag_str}

## Problem

> {summary}

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```{fence}
{code.strip()}
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #{number} {title} -->
"""

    os.makedirs(PROBLEMS_DIR, exist_ok=True)
    fname = safe_filename(number, title)
    path = os.path.join(PROBLEMS_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(note)
    return fname


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cookie", required=True,
                        help='Value of your LEETCODE_SESSION cookie')
    parser.add_argument("--skip-existing", action="store_true", default=True,
                        help="Skip problems that already have a note file")
    args = parser.parse_args()

    session = requests.Session()
    session.headers.update(HEADERS)
    session.cookies.set("LEETCODE_SESSION", args.cookie, domain=".leetcode.com")

    # Fetch csrftoken by hitting the homepage
    session.get("https://leetcode.com")
    csrf = session.cookies.get("csrftoken", domain=".leetcode.com") or \
           session.cookies.get("csrftoken")
    if csrf:
        session.headers["x-csrftoken"] = csrf
        print(f"  CSRF token acquired.")

    print(f"Fetching all AC problems for {USERNAME}...")
    problems = fetch_all_solved_problems(session)

    created = 0
    skipped = 0
    for prob in problems:
        slug = prob["titleSlug"]
        title = prob["title"]
        number = prob.get("frontendId", "?")

        if args.skip_existing and note_exists(number, title):
            print(f"  Skipping {number}. {title} (exists)")
            skipped += 1
            continue

        print(f"  Processing: {number}. {title}", end=" ", flush=True)

        # Get latest AC submission for this problem
        sub_id, lang = fetch_latest_ac_submission(session, slug)
        time.sleep(0.3)

        # Get full problem details (description)
        detail = fetch_problem_detail(session, slug)
        # Merge tags from progress list (already have them) into detail
        if not detail.get("topicTags") and prob.get("topicTags"):
            detail["topicTags"] = prob["topicTags"]
        time.sleep(0.3)

        code = ""
        if sub_id:
            code, lang = fetch_submission_code(session, sub_id)
            time.sleep(0.3)

        fname = write_note(detail, code, lang or "python3")
        print(f"→ {fname}")
        created += 1

    print(f"\nDone. Created: {created}, Skipped: {skipped}")
    print("Run `git add problems/ && git commit -m 'add: import leetcode submissions'` to save.")


if __name__ == "__main__":
    main()
