# 2461. Maximum Sum of Distinct Subarrays With Length K

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Sliding Window`

## Problem

> You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:   	The length of the subarray is k, and 	All the elements of the subarray are distinct.   Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.  A subarray is a contiguous non-emp...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        ans = 0
        s = 0
        for i, num in enumerate(nums):
            s += num
            cnt[num] += 1
            if i - k + 1 < 0:
                continue
            if len(cnt) == k:
                ans = max(ans, s)
            s -= nums[i - k + 1]
            cnt[nums[i - k + 1]] -= 1
            if cnt[nums[i - k + 1]] == 0:
                del cnt[nums[i - k + 1]]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2461 Maximum Sum of Distinct Subarrays With Length K -->
