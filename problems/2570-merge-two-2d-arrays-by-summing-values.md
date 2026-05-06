# 2570. Merge Two 2D Arrays by Summing Values

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Two Pointers`

## Problem

> You are given two 2D integer arrays nums1 and nums2.   	nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali. 	nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.   Each array contains unique ids and is sorted in ascending order by id.  Merge the two arrays into one array that is sorted in ascending order by id, respecting...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        a = b = 0
        ans = []
        while a < m and b < n:
            if nums1[a][0] < nums2[b][0]:
                ans.append(nums1[a])
                a += 1
            elif nums2[b][0] < nums1[a][0]:
                ans.append(nums2[b])
                b += 1
            else:
                nums1[a][1] += nums2[b][1]
                ans.append(nums1[a])
                a += 1
                b += 1
        while a < m:
            ans.append(nums1[a])
            a += 1
        while b < n:
            ans.append(nums2[b])
            b += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2570 Merge Two 2D Arrays by Summing Values -->
