# 525. Contiguous Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Prefix Sum`

## Problem

> Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.    Example 1:   Input: nums = [0,1] Output: 2 Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.   Example 2:   Input: nums = [0,1,0] Output: 2 Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.   Example 3:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans  = 0
        cnt = {0: -1}
        diff = 0
        for i, num in enumerate(nums):
            if num == 0:
                diff += 1
            else:
                diff -= 1
            if diff in cnt:
                ans = max(ans, i - cnt[diff])
            else:
                cnt[diff] = i
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #525 Contiguous Array -->
