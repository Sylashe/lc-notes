# 2730. Find the Longest Semi-Repetitive Substring

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String` `Sliding Window`

## Problem

> You are given a digit string s that consists of digits from 0 to 9.  A string is called semi-repetitive if there is at most one adjacent pair of the same digit. For example, "0010", "002020", "0123", "2002", and "54944" are semi-repetitive while the following are not: "00101022" (adjacent same digit pairs are 00 and 22), and "1101234883" (adjacent same digit pairs are 11 and 88).  Return the lengt...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        cnt = 0
        left = 0
        ans = 0
        for right,num in enumerate(s):
            if right > 0:
                if num == s[right - 1]:
                    cnt += 1
            while cnt > 1:
                if s[left] == s[left + 1]:
                    cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2730 Find the Longest Semi-Repetitive Substring -->
