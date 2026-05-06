# 1695. Maximum Erasure Value

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Sliding Window`

## Problem

> You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.  Return the maximum score you can get by erasing exactly one subarray.  An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cnt = set()
        ans = 0
        s = 0
        l = 0
        for r, num in enumerate(nums):
            while num in cnt:
                cnt.remove(nums[l])
                s -= nums[l]
                l += 1
            s += num
            cnt.add(num)
            ans = max(ans, s)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1695 Maximum Erasure Value -->
