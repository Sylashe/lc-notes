# 674. Longest Continuous Increasing Subsequence

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array`

## Problem

> Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.  A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].    Example 1:   Input: nums = [1,3,5...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0 
        cnt = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
        return max(ans, cnt)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #674 Longest Continuous Increasing Subsequence -->
