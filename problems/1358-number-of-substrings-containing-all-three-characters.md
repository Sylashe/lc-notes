# 1358. Number of Substrings Containing All Three Characters

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Hash Table` `String` `Sliding Window`

## Problem

> Given a string s consisting only of characters a, b and c.  Return the number of substrings containing at least one occurrence of all these characters a, b and c.    Example 1:   Input: s = "abcabc" Output: 10 Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again)....

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = Counter()
        l = 0
        ans = 0
        for r, c in enumerate(s):
            cnt[c] += 1
            while len(cnt) == 3:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1
            ans += l
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1358 Number of Substrings Containing All Three Characters -->
