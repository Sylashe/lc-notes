# 1759. Count Number of Homogenous Substrings

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Math` `String`

## Problem

> Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.  A string is homogenous if all the characters of the string are the same.  A substring is a contiguous sequence of characters within a string.    Example 1:   Input: s = "abbcccaa" Output: 13 Explanation: The homogenous substrings are listed as below: "a"   appears 3 time...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        cnt = 0
        mod = 10 ** 9 + 7
        for i, c in enumerate(s):
            if i == 0 or c == s[i - 1]:
                cnt += 1
            else:
                cnt = 1
            ans += cnt
        return ans % mod
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1759 Count Number of Homogenous Substrings -->
