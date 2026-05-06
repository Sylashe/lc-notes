# 350. Intersection of Two Arrays II

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Two Pointers` `Binary Search` `Sorting`

## Problem

> Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.    Example 1:   Input: nums1 = [1,2,2,1], nums2 = [2,2] Output: [2,2]   Example 2:   Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4] Output: [4,9] Explanation: [9,4] is also accepted.     Constraints...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        a = b = 0
        ans = []
        while a < m and b < n:
            if nums1[a] < nums2[b]:
                a += 1
            elif nums2[b] < nums1[a]:
                b += 1
            else:
                ans.append(nums1[a])
                a += 1
                b += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #350 Intersection of Two Arrays II -->
