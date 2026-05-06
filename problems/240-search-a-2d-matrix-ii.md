# 240. Search a 2D Matrix II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search` `Divide and Conquer` `Matrix`

## Problem

> Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:   	Integers in each row are sorted in ascending from left to right. 	Integers in each column are sorted in ascending from top to bottom.     Example 1:   Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5 O...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)
        i = 0
        j = n - 1
        while i < m and j >=0 :
            x = matrix[i][j]
            if x == target:
                return True
            elif x < target:
                i += 1
            else:
                j -= 1
        return False
```

## Complexity

- Time: O()
- Space: O()

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #240 Search a 2D Matrix II -->
