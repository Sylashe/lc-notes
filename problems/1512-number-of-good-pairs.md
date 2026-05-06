# 1512. Number of Good Pairs

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Math` `Counting`

## Problem

> Given an array of integers nums, return the number of good pairs.  A pair (i, j) is called good if nums[i] == nums[j] and i < j.    Example 1:   Input: nums = [1,2,3,1,1,3] Output: 4 Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.   Example 2:   Input: nums = [1,1,1,1] Output: 6 Explanation: Each pair in the array are good.   Example 3:   Input: nums = [1,2,3] Output: 0...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        for i in range(0,n):
            for o in range(i+1,n):
                if nums[i] == nums[o]:
                    cnt +=1
        return cnt
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1512 Number of Good Pairs -->
