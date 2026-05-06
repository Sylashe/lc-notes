# 496. Next Greater Element I

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Stack` `Monotonic Stack`

## Problem

> The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.  You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.  For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next great...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        mp = dict()
        for i, num in enumerate(nums2):
            while st and st[-1] < num:
                value = st.pop()
                mp[value] = num
            st.append(num)
        for i, num in enumerate(nums1):
            if num in mp:
                nums1[i] = mp[num]
            else:
                nums1[i] = -1
        return nums1
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #496 Next Greater Element I -->
