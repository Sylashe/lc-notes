# 697. Degree of an Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table`

## Problem

> Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.  Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.    Example 1:   Input: nums = [1,2,2,3,1] Output: 2 Explanation:  The input array has a degree of 2 because both elements 1 and 2 appea...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = dict()
        degree = 0
        ans = len(nums)
        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1
                mp[num][2] = i
            else:
                mp[num] = [1, i, i]
            degree = max(degree, mp[num][0])
        for num in mp:
            if mp[num][0] == degree:
                ans = min(ans, mp[num][2] - mp[num][1] + 1)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #697 Degree of an Array -->
