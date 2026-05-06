# 2760. Longest Even Odd Subarray With Threshold

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Sliding Window`

## Problem

> You are given a 0-indexed integer array nums and an integer threshold.  Find the length of the longest subarray of nums starting at index l and ending at index r (0 <= l <= r < nums.length) that satisfies the following conditions:   	nums[l] % 2 == 0 	For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2 	For all indices i in the range [l, r], nums[i] <= threshold   Return an i...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        cnt = 0
        i = 0
        start = 0
        while i < len(nums):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                start = i
                while i < len(nums) - 1 and nums[i + 1] <= threshold and nums[i] % 2 != nums[i + 1] % 2:
                    i += 1
                ans = max(ans, i - start + 1)
            i += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2760 Longest Even Odd Subarray With Threshold -->
