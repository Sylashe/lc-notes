# 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Math` `Two Pointers`

## Problem

> Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:   	Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length. 	Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.     Example 1:   Input:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        def TripletCount(nums1, nums2) -> int:
            ans = 0
            n = len(nums1)
            for i in range(n):
                j = 0
                k = len(nums2) - 1
                target = nums1[i] ** 2
                while j < k:
                    if nums2[j] * nums2[k] < target:
                        j += 1
                    elif nums2[j] * nums2[k] > target:
                        k -= 1
                    else:
                        if nums2[j] == nums2[k]:
                            m = k - j + 1
                            ans += m * (m - 1) // 2
                            break
                        rep, rep1 = 1, 1
                        j += 1
                        while j < k and nums2[j] == nums2[j - 1]:
                            rep += 1
                            j += 1
                        while k > j and nums2[k] == nums2[k - 1]:
                            rep1 += 1
                            k -= 1 
                        ans += rep * rep1
            return ans
        return TripletCount(nums1, nums2) + TripletCount(nums2, nums1)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1577 Number of Ways Where Square of Number Is Equal to Product of Two Numbers -->
