# 696. Count Binary Substrings

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Two Pointers` `String`

## Problem

> Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.  Substrings that occur multiple times are counted the number of times they occur.    Example 1:   Input: s = "00110011" Output: 6 Explanation: There are 6 substrings that have equal number of consecutive 1's and...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        cnt = 0
        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                cnt += 1
            else:
                groups.append(cnt)
                cnt = 1
        ans = 0
        groups.append(cnt)
        for j, c in enumerate(groups):
            if j == 0:
                continue
            ans += min(c, groups[j - 1])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #696 Count Binary Substrings -->
