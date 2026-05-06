# 852. Peak Index in a Mountain Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search`

## Problem

> You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.  Return the index of the peak element.  Your task is to solve it in O(log(n)) time complexity.    Example 1:   Input: arr = [0,1,0]  Output: 1   Example 2:   Input: arr = [0,2,1,0]  Output: 1   Example 3:   Input: arr = [0,10,5,2]  Output: 1     Constraints:   	3 <= arr.length <=...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #852 Peak Index in a Mountain Array -->
