# 485. Max Consecutive Ones

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array`

## Problem

> Given a binary array nums, return the maximum number of consecutive 1's in the array.    Example 1:   Input: nums = [1,1,0,1,1,1] Output: 3 Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.   Example 2:   Input: nums = [1,0,1,1,0,1] Output: 2     Constraints:   	1 <= nums.length <= 105 	nums[i] is either 0 or 1.

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                cnt += 1
            else:
                ans = max(cnt, ans)
                cnt = 0
        return max(ans, cnt)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #485 Max Consecutive Ones -->
