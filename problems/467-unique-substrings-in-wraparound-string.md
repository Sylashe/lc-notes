# 467. Unique Substrings in Wraparound String

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String` `Dynamic Programming`

## Problem

> We define the string base to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so base will look like this:   	"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".   Given a string s, return the number of unique non-empty substrings of s are present in base.    Example 1:   Input: s = "a" Output: 1 Explanation: Only the substring "a" of s is in base.   Example 2:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = [0] * 26
        cnt = 0
        ans = 0
        for i in range(len(s)):
            if i == 0 or ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i]) - ord(s[i - 1]) == -25:
                cnt += 1
            else:
                cnt = 1
            idx = ord(s[i]) - ord("a")
            dp[idx] = max(dp[idx], cnt)
        return sum(dp)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #467 Unique Substrings in Wraparound String -->
