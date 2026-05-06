# 3427. Sum of Variable Length Subarrays

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Prefix Sum`

## Problem

> You are given an integer array nums of size n. For each index i where 0 <= i < n, define a subarray nums[start ... i] where start = max(0, i - nums[i]).  Return the total sum of all elements from the subarray defined for each index in the array.    Example 1:   Input: nums = [2,3,1]  Output: 11  Explanation:   	 		 			i 			Subarray 			Sum 		 		 			0 			nums[0] = [2] 			2 		 		 			1 			nums[0 ... 1...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        pre_sum = [0] * (len(nums) + 1)
        ans = 0
        for i, num in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + num
        for i, num in enumerate(nums):
            ans += pre_sum[i + 1] - pre_sum[max(0, i - nums[i])]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3427 Sum of Variable Length Subarrays -->
