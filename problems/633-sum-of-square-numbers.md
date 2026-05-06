# 633. Sum of Square Numbers

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Math` `Two Pointers` `Binary Search`

## Problem

> Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.    Example 1:   Input: c = 5 Output: true Explanation: 1 * 1 + 2 * 2 = 5   Example 2:   Input: c = 3 Output: false     Constraints:   	0 <= c <= 231 - 1

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        upper_bound = c ** 0.5
        if int(upper_bound) == upper_bound :
            return True
        else:
            upper_bound = int(upper_bound)
        lower_bound = 1
        while lower_bound <= upper_bound:
            if lower_bound ** 2 + upper_bound ** 2 < c:
                lower_bound += 1
            elif lower_bound ** 2 + upper_bound ** 2 > c:
                upper_bound -= 1
            else:
                return True
        return False
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #633 Sum of Square Numbers -->
