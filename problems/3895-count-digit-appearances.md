# 3895. Count Digit Appearances

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** 

## Problem

> You are given an integer array nums and an integer digit.  Return the total number of times digit appears in the decimal representation of all elements in nums.    Example 1:   Input: nums = [12,54,32,22], digit = 2  Output: 4  Explanation:  The digit 2 appears once in 12 and 32, and twice in 22. Thus, the total number of times digit 2 appears is 4.   Example 2:   Input: nums = [1,34,7], digit = 9...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        ans = 0
        for num in nums:
            for digits in str(num):
                if digits == str(digit):
                    ans += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3895 Count Digit Appearances -->
