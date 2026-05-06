# 16. 3Sum Closest

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Sorting`

## Problem

> Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.  Return the sum of the three integers.  You may assume that each input would have exactly one solution.    Example 1:   Input: nums = [-1,2,1,-4], target = 1 Output: 2 Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).   Exam...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = float('inf')
        if nums[0] + nums[1] + nums[2] > target:
            return nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(ans - target):
                    ans = s
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    return target
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #16 3Sum Closest -->
