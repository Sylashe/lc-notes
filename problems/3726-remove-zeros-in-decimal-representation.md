# 3726. Remove Zeros in Decimal Representation

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Math` `Simulation`

## Problem

> You are given a positive integer n.  Return the integer obtained by removing all zeros from the decimal representation of n.    Example 1:   Input: n = 1020030  Output: 123  Explanation:  After removing all zeros from 1020030, we get 123.   Example 2:   Input: n = 1  Output: 1  Explanation:  1 has no zero in its decimal representation. Therefore, the answer is 1.     Constraints:   	1 <= n <= 1015

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def removeZeros(self, n: int) -> int:
        n = str(n)
        ans = ""
        for char in n:
            if char != "0":
                ans+=char
        return int(ans)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3726 Remove Zeros in Decimal Representation -->
