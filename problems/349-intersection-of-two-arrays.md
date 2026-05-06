# 349. Intersection of Two Arrays

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Two Pointers` `Binary Search` `Sorting`

## Problem

> Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.    Example 1:   Input: nums1 = [1,2,2,1], nums2 = [2,2] Output: [2]   Example 2:   Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4] Output: [9,4] Explanation: [4,9] is also accepted.     Constraints:   	1 <= nums1.length, nums2.length <=...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        set2 = set(nums2)
        for num in nums1:
            if num in set2:
                ans.add(num)
        return list(ans)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #349 Intersection of Two Arrays -->
