# 1234. Replace the Substring for Balanced String

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String` `Sliding Window`

## Problem

> You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.  A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.  Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.    Example 1:   Inp...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        m = len(s)/4
        l = 0
        ans = len(s) + 1
        if len(cnt) == 4 and min(cnt.values()) == m:
            return 0
        for r, c in enumerate(s):
            cnt[c] -= 1
            while max(cnt.values()) <= m:
                ans = min(ans, r - l + 1)
                cnt[s[l]] += 1
                l += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1234 Replace the Substring for Balanced String -->
