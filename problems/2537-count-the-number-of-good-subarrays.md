# 2537. Count the Number of Good Subarrays

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Sliding Window`

## Problem

> Given an integer array nums and an integer k, return the number of good subarrays of nums.  A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].  A subarray is a contiguous non-empty sequence of elements within an array.    Example 1:   Input: nums = [1,1,1,1,1], k = 10 Output: 1 Explanation: The only good subarray is the array nums itself....

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        l = 0
        pairs = 0
        for r, num in enumerate(nums):
            pairs += cnt[num]
            cnt[num] += 1
            while pairs >= k:
                cnt[nums[l]] -= 1
                pairs -= cnt[nums[l]]
                l += 1
            ans += l
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2537 Count the Number of Good Subarrays -->
