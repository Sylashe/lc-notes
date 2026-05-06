# 3917. Count Indices With Opposite Parity

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** 

## Problem

> You are given an integer array nums of length n.  The score of an index i is defined as the number of indices j such that:   	i < j < n, and 	nums[i] and nums[j] have different parity (one is even and the other is odd).   Return an integer array answer of length n, where answer[i] is the score of index i.    Example 1:   Input: nums = [1,2,3,4]  Output: [2,1,1,0]  Explanation:   	nums[0] = 1, whic...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        even_cnt = (n + 1) * [0]
        odd_cnt = (n + 1) * [0]
        for i in range(n - 1, -1, -1):
            if nums[i] % 2 == 0:
                even_cnt[i] = even_cnt[i + 1] + 1
                odd_cnt[i] = odd_cnt[i + 1]
            else:
                odd_cnt[i] = odd_cnt[i + 1] + 1
                even_cnt[i] = even_cnt[i + 1]
        ans = n * [0]
        for idx in range(n):
            if nums[idx] % 2 == 0:
                ans[idx] = odd_cnt[idx]
            else:
                ans[idx] = even_cnt[idx]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3917 Count Indices With Opposite Parity -->
