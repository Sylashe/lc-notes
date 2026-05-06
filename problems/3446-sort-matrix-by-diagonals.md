# 3446. Sort Matrix by Diagonals

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Sorting` `Matrix`

## Problem

> You are given an n x n square matrix of integers grid. Return the matrix such that:   	The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order. 	The diagonals in the top-right triangle are sorted in non-decreasing order.     Example 1:   Input: grid = [[1,7,3],[9,8,2],[4,5,6]]  Output: [[8,2,3],[9,6,7],[4,5,1]]  Explanation:    The diagonals wit...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n):
            diagonal = []
            row, col = i, 0
            while row < n and col < n:
                diagonal.append(grid[row][col])
                row += 1
                col += 1
            diagonal.sort(reverse=True)
            row, col = i, 0
            idx = 0
            while row < n and col < n:
                grid[row][col] = diagonal[idx]
                row += 1
                col += 1
                idx += 1
        for j in range(1, n):
            diagonal = []
            row, col = 0, j
            while row < n and col < n:
                diagonal.append(grid[row][col])
                row += 1
                col += 1
            diagonal.sort()
            row, col = 0, j
            idx = 0
            while row < n and col < n:
                grid[row][col] = diagonal[idx]
                row += 1
                col += 1
                idx += 1
        
        return grid
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3446 Sort Matrix by Diagonals -->
