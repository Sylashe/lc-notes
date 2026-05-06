# 1493. Longest Subarray of 1's After Deleting One Element

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Dynamic Programming` `Sliding Window`

## Problem

> Given a binary array nums, you should delete one element from it.  Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.    Example 1:   Input: nums = [1,1,0,1] Output: 3 Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.   Example 2:   Input: nums = [0,1,1,1,0,1,1,0,1] O...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        zero_cnt = 0
        for right, num in enumerate(nums):
            if num == 0:
                zero_cnt += 1
            while zero_cnt > 1:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            ans = max(ans, right - left)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1493 Longest Subarray of 1's After Deleting One Element -->
