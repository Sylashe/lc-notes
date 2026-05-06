# 1461. Check If a String Contains All Binary Codes of Size K

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Hash Table` `String` `Bit Manipulation` `Rolling Hash` `Hash Function`

## Problem

> Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.    Example 1:   Input: s = "00110110", k = 2 Output: true Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.   Example 2:   Input: s = "0110", k = 1 Output: true Explanat...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ans = 2 ** k
        seen = set()
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            seen.add(substring)
        return len(seen) == ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1461 Check If a String Contains All Binary Codes of Size K -->
