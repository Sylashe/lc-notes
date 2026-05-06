# 3350. Adjacent Increasing Subarrays Detection II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search`

## Problem

> Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:   	Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing. 	The subarrays must...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        pre_cnt = 0
        for i, num in enumerate(nums):
            if i == 0 or nums[i - 1] < nums[i]:
                cnt += 1
            else:
                pre_cnt = cnt
                cnt = 1
            if pre_cnt >= cnt:
                ans = max(ans, cnt)
            if cnt % 2 == 0:
                ans = max(ans, cnt // 2)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3350 Adjacent Increasing Subarrays Detection II -->
