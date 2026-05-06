# 2762. Continuous Subarrays

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Queue` `Sliding Window` `Heap (Priority Queue)` `Ordered Set` `Monotonic Queue`

## Problem

> You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:   	Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.   Return the total number of continuous subarrays.  A subarray is a contiguous non-empty sequence of elements within an array.    Example 1:   Input: nums = [5,4,2,4] Outpu...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = ans = 0
        cnt = defaultdict(int)
        for r,num in enumerate(nums):
            cnt[num] += 1
            while max(cnt) - min(cnt) > 2:
                cnt[nums[l]] -= 1
                if cnt[nums[l]] == 0:
                    del cnt[nums[l]]
                l += 1
            ans += r - l + 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2762 Continuous Subarrays -->
