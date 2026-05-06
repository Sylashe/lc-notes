# 2389. Longest Subsequence With Limited Sum

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Binary Search` `Greedy` `Sorting` `Prefix Sum`

## Problem

> You are given an integer array nums of length n, and an integer array queries of length m.  Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].  A subsequence is an array that can be derived from another array by deleting some or no elements without changing the or...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        #<=
        nums.sort()
        ans = [0] * len(queries)
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        for i, num in enumerate(queries):
            l = 0
            r = len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] > num:
                    r = m - 1
                else:
                    l = m + 1
            ans[i] = l
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2389 Longest Subsequence With Limited Sum -->
