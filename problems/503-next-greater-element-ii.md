# 503. Next Greater Element II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Stack` `Monotonic Stack`

## Problem

> Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.  The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.    Example 1:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        st = []
        n = len(nums)
        for i in range(2 * n):
            while st and nums[st[-1]] < nums[i % n]:
                ans[st.pop()] = nums[i % n]
            if i < n:
                st.append(i)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #503 Next Greater Element II -->
