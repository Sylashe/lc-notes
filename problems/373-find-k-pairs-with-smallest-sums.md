# 373. Find K Pairs with Smallest Sums

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Heap (Priority Queue)`

## Problem

> You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.  Define a pair (u, v) which consists of one element from the first array and one element from the second array.  Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.    Example 1:   Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3 Output: [[1,2],[1,4],[1,6]] Explanation: The fir...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m = len(nums1)
        n = len(nums2)
        pq = []
        ans = []
        for i in range(min(m, k)):
            heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))
        while pq and len(ans) < k:
            _, indx1, indx2 = heapq.heappop(pq)
            ans.append([nums1[indx1], nums2[indx2]])
            if indx2 < n - 1:
                heapq.heappush(pq, (nums1[indx1] + nums2[indx2 + 1], indx1, indx2 + 1))
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #373 Find K Pairs with Smallest Sums -->
