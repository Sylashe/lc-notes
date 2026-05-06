# 1281. Subtract the Product and Sum of Digits of an Integer

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Math`

## Problem

> Given an integer number n, return the difference between the product of its digits and the sum of its digits.   Example 1:   Input: n = 234 Output: 15  Explanation:  Product of digits = 2 * 3 * 4 = 24  Sum of digits = 2 + 3 + 4 = 9  Result = 24 - 9 = 15   Example 2:   Input: n = 4421 Output: 21 Explanation:  Product of digits = 4 * 4 * 2 * 1 = 32  Sum of digits = 4 + 4 + 2 + 1 = 11  Result = 32 -...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum, product = 0, 1
        while n:
            product *= n%10
            sum += n%10
            n //= 10
        return product - sum
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1281 Subtract the Product and Sum of Digits of an Integer -->
