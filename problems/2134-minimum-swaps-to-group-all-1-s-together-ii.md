# 2134. Minimum Swaps to Group All 1's Together II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Sliding Window`

## Problem

> A swap is defined as taking two distinct positions in an array and swapping the values in them.  A circular array is defined as an array where we consider the first element and the last element to be adjacent.  Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.    Example 1:   Input: nums = [0,1,0,1,1,0,0]...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ans = sum(nums)
        n = len(nums)
        k = ans
        r = k - 1
        s = sum(nums[:r])
        for i in range(n):
            s += nums[(i+r)%n]
            ans = min(ans,k-s)
            s -= nums[i]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2134 Minimum Swaps to Group All 1's Together II -->
