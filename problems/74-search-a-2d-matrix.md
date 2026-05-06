# 74. Search a 2D Matrix

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search` `Matrix`

## Problem

> You are given an m x n integer matrix matrix with the following two properties:   	Each row is sorted in non-decreasing order. 	The first integer of each row is greater than the last integer of the previous row.   Given an integer target, return true if target is in matrix or false otherwise.  You must write a solution in O(log(m * n)) time complexity.    Example 1:   Input: matrix = [[1,3,5,7],[1...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            mid = l + (r - l)//2
            x = matrix[mid//n][mid%n]
            if x == target:
                return True
            elif x > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #74 Search a 2D Matrix -->
