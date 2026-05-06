# 2765. Longest Alternating Subarray

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Enumeration`

## Problem

> You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:   	m is greater than 1. 	s1 = s0 + 1. 	The 0-indexed subarray s looks like [s0, s1, s0, s1,...,s(m-1) % 2]. In other words, s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1, and so on up to s[m - 1] - s[m - 2] = (-1)m.   Return the maximum length of all alternating subarrays present in nums or -1 i...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] + 1 != nums[i + 1]:
                i += 1
                continue
            start_i = i
            i += 2
            while i < n and nums[i] == nums[i - 2]:
                i += 1
            ans = max(ans, i - start_i)
            i -= 1
        return ans if ans != 0 else -1
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2765 Longest Alternating Subarray -->
