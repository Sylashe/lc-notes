# 2090. K Radius Subarray Averages

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Sliding Window`

## Problem

> You are given a 0-indexed array nums of n integers, and an integer k.  The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.  Build and return an array avgs of length n where avgs[i]...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        q = 2*k + 1
        s = 0
        ans = [-1] * len(nums)
        for i, num in enumerate(nums):
            s += num
            if i - q + 1 < 0:
                continue
            ans[i - k] = s // q
            s -= nums[i - q + 1]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2090 K Radius Subarray Averages -->
