# 1984. Minimum Difference Between Highest and Lowest of K Scores

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Sliding Window` `Sorting`

## Problem

> You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.  Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.  Return the minimum possible difference.    Example 1:   Input: nums = [90], k = 1 Output: 0 Explanation: There is one way to pi...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(k - 1, len(nums)):
            ans = min(ans, nums[i] - nums[i - k + 1])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1984 Minimum Difference Between Highest and Lowest of K Scores -->
