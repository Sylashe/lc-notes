# 3712. Sum of Elements With Frequency Divisible by K

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Counting`

## Problem

> You are given an integer array nums and an integer k.  Return an integer denoting the sum of all elements in nums whose frequency is divisible by k, or 0 if there are no such elements.  Note: An element is included in the sum exactly as many times as it appears in the array if its total frequency is divisible by k.    Example 1:   Input: nums = [1,2,2,3,3,3,3,4], k = 2  Output: 16  Explanation:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        ans = 0
        num_dict = Counter(nums)
        for i, num in enumerate(num_dict):
            if num_dict[num] % k == 0:
                ans += num_dict[num] * num
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3712 Sum of Elements With Frequency Divisible by K -->
