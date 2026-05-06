# 1513. Number of Substrings With Only 1s

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Math` `String`

## Problem

> Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.    Example 1:   Input: s = "0110111" Output: 9 Explanation: There are 9 substring in total with only 1's characters. "1" -> 5 times. "11" -> 3 times. "111" -> 1 time.  Example 2:   Input: s = "101" Output: 2 Explanation: Substring "1" is shown 2 times in s....

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        ans = 0
        for c in s:
            if c == "1":
                cnt += 1
                ans += cnt
            else:
                cnt = 0
        return ans % (10 ** 9 + 7)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1513 Number of Substrings With Only 1s -->
