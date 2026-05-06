# 1574. Shortest Subarray to be Removed to Make Array Sorted

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Binary Search` `Stack` `Monotonic Stack`

## Problem

> Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.  Return the length of the shortest subarray to remove.  A subarray is a contiguous subsequence of the array.    Example 1:   Input: arr = [1,2,3,10,4,2,3,5] Output: 3 Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        ans = 0
        r = len(arr) - 1
        while r >= 1 and arr[r] >= arr[r - 1]:
            r -= 1
        if r == 0:
            return 0
        ans = r
        l = 0
        while l == 0 or arr[l - 1] <= arr[l]:
            while r < len(arr) and arr[l] > arr[r]:
                r += 1
            ans = min(ans, r - l - 1)
            l += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1574 Shortest Subarray to be Removed to Make Array Sorted -->
