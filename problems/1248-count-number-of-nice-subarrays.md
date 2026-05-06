# 1248. Count Number of Nice Subarrays

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Math` `Sliding Window` `Prefix Sum`

## Problem

> Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.  Return the number of nice sub-arrays.    Example 1:   Input: nums = [1,1,2,1,1], k = 3 Output: 2 Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].   Example 2:   Input: nums = [2,4,6], k = 1 Output: 0 Explanation: There are no odd numbers in the a...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i, num in enumerate(nums):
            nums[i] = 1 if nums[i] % 2 == 1 else 0
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        ans = 0
        pre_fix = 0
        for num in nums:
            pre_fix += num
            if pre_fix - k >= 0:
                ans += cnt[pre_fix - k]
            cnt[pre_fix] += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1248 Count Number of Nice Subarrays -->
