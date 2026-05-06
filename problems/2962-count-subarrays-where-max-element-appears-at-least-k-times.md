# 2962. Count Subarrays Where Max Element Appears at Least K Times

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Sliding Window`

## Problem

> You are given an integer array nums and a positive integer k.  Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.  A subarray is a contiguous sequence of elements within an array.    Example 1:   Input: nums = [1,3,2,3,3], k = 2 Output: 6 Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_in_nums = max(nums)
        ans = 0
        l = 0
        max_cnt = 0
        for r, num in enumerate(nums):
            if num == max_in_nums:
                max_cnt += 1
            while max_cnt == k:
                if nums[l] == max_in_nums:
                    max_cnt -= 1
                l += 1
            ans += l
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2962 Count Subarrays Where Max Element Appears at Least K Times -->
