# 2302. Count Subarrays With Score Less Than K

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Array` `Binary Search` `Sliding Window` `Prefix Sum`

## Problem

> The score of an array is defined as the product of its sum and its length.   	For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.   Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.  A subarray is a contiguous sequence of elements within an array.    Example 1:   Input: nums = [2,1,4,3,...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = l = 0
        sum = 0
        for r, num in enumerate(nums):
            sum += num
            while sum * (r - l + 1) >= k:
                sum -= nums[l]
                l += 1
            ans += r - l + 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2302 Count Subarrays With Score Less Than K -->
