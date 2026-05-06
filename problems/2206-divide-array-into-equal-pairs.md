# 2206. Divide Array Into Equal Pairs

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Bit Manipulation` `Counting`

## Problem

> You are given an integer array nums consisting of 2 * n integers.  You need to divide nums into n pairs such that:   	Each element belongs to exactly one pair. 	The elements present in a pair are equal.   Return true if nums can be divided into n pairs, otherwise return false.    Example 1:   Input: nums = [3,2,3,2,2,2] Output: true Explanation:  There are 6 elements in nums, so they should be div...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                return False
            else:
                i += 2
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2206 Divide Array Into Equal Pairs -->
