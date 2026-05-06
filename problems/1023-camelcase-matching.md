# 1023. Camelcase Matching

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `String` `Trie` `String Matching`

## Problem

> Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.  A query word queries[i] matches pattern if you can insert lowercase English letters into the pattern so that it equals the query. You may insert a character at any position in pattern or you may choose not to insert any characters at all...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(query, pattern) -> bool:
            i = 0
            for j, c in enumerate(query):
                if i < len(pattern) and c == pattern[i]:
                    i += 1
                elif c .isupper():
                    return False
            return i == len(pattern)
        ans = len(queries) * [False]
        for i in range(len(queries)):
            ans[i] = check(queries[i], pattern)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1023 Camelcase Matching -->
