# 3918. Sum of Primes Between Number and Its Reverse

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** 

## Problem

> You are given an integer n.  Let r be the integer formed by reversing the digits of n.  Return the sum of all prime numbers between min(n, r) and max(n, r), inclusive.    Example 1:   Input: n = 13  Output: 132  Explanation:   	The reverse of 13 is 31. Thus, the range is [13, 31]. 	The prime numbers in this range are 13, 17, 19, 23, 29, and 31. 	The sum of these prime numbers is 13 + 17 + 19 + 23...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
        cpy = n
        res = 0
        while cpy > 0:
            res = res * 10 + cpy % 10
            cpy //= 10
        l = min(n, res)
        r = max(n, res)
        ans = 0
        for x in range(l, r + 1):
            if is_prime(x):
                ans += x
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3918 Sum of Primes Between Number and Its Reverse -->
