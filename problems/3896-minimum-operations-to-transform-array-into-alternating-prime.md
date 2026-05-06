# 3896. Minimum Operations to Transform Array into Alternating Prime

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** 

## Problem

> You are given an integer array nums.  An array is considered alternating prime if:   	Elements at even indices (0-based) are prime numbers. 	Elements at odd indices are non-prime numbers.   In one operation, you may increment any element by 1.  Return the minimum number of operations required to transform nums into an alternating prime array.  A prime number is a natural number greater than 1 with...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def is_prime(x):
            if x <= 1:
                return False
            for num in range(2,int(sqrt(x)) + 1):
                if x % num == 0:
                    return False
            return True
        ans = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                while is_prime(num) == False:
                    ans += 1
                    num += 1
            else:
                while is_prime(num) == True:
                    ans += 1
                    num += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3896 Minimum Operations to Transform Array into Alternating Prime -->
