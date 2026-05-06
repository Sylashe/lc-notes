# 2958. Length of Longest Subarray With at Most K Frequency

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Sliding Window`

## Problem

> You are given an integer array nums and an integer k.  The frequency of an element x is the number of times it occurs in an array.  An array is called good if the frequency of each element in this array is less than or equal to k.  Return the length of the longest good subarray of nums.  A subarray is a contiguous non-empty sequence of elements within an array.    Example 1:   Input: nums = [1,2,3...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        cnt = defaultdict(int)
        for right, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2958 Length of Longest Subarray With at Most K Frequency -->
