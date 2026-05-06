# 3432. Count Partitions with Even Sum Difference

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Math` `Prefix Sum`

## Problem

> You are given an integer array nums of length n.  A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:   	Left subarray contains indices [0, i]. 	Right subarray contains indices [i + 1, n - 1].   Return the number of partitions where the difference between the sum of the left and right subarrays is even.    Example 1:   Input: nums...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        if sum(nums) % 2 == 0:
            return len(nums) - 1
        else:
            return 0
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3432 Count Partitions with Even Sum Difference -->
