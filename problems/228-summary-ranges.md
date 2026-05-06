# 228. Summary Ranges

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array`

## Problem

> You are given a sorted unique integer array nums.  A range [a,b] is the set of all integers from a to b (inclusive).  Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.  Each range [a,b] in the list should be o...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while i < len(nums):
            start = i
            s = str(nums[i])
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            if start < i:
                s += "->"
                s += str(nums[i])
            ans.append(s)
            i += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #228 Summary Ranges -->
