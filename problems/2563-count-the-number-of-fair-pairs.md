# 2563. Count the Number of Fair Pairs

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Binary Search` `Sorting`

## Problem

> Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.  A pair (i, j) is fair if:   	0 <= i < j < n, and 	lower <= nums[i] + nums[j] <= upper     Example 1:   Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6 Output: 6 Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).   Example 2:   Input: nums = [1,7,9,2,5...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def helper(nums, limit):
            i = 0
            j = len(nums) - 1
            ans = 0
            while i < j:
                if nums[i] + nums[j] > limit:
                    j -= 1
                else:
                    ans += j - i
                    i += 1
            return ans
        return helper(nums, upper) - helper(nums, lower - 1)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2563 Count the Number of Fair Pairs -->
