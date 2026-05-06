# 2841. Maximum Sum of Almost Unique Subarray

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Sliding Window`

## Problem

> You are given an integer array nums and two positive integers m and k.  Return the maximum sum out of all almost unique subarrays of length k of nums. If no such subarray exists, return 0.  A subarray of nums is almost unique if it contains at least m distinct elements.  A subarray is a contiguous non-empty sequence of elements within an array.    Example 1:   Input: nums = [2,6,7,3,1,7], m = 3, k...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cnt = Counter()
        s = 0
        ans = 0
        for i, num in enumerate(nums):
            s += num
            cnt[num] += 1
            if i - k + 1 < 0:
                continue
            if len(cnt) >= m:
                ans = max(ans, s)
            s -= nums[i - k + 1]
            cnt[nums[i - k + 1]] -= 1
            if cnt[nums[i - k + 1]] == 0:
                del cnt[nums[i - k + 1]]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2841 Maximum Sum of Almost Unique Subarray -->
