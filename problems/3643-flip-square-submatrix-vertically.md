# 3643. Flip Square Submatrix Vertically

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers` `Matrix`

## Problem

> You are given an m x n integer matrix grid, and three integers x, y, and k.  The integers x and y represent the row and column indices of the top-left corner of a square submatrix and the integer k represents the size (side length) of the square submatrix.  Your task is to flip the submatrix by reversing the order of its rows vertically.  Return the updated matrix.    Example 1:   Input: grid = [[...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l, r = x, x + k - 1
        while l < r:
            for j in range(y, y + k):
                grid[l][j], grid[r][j] = grid[r][j], grid[l][j]
            l += 1
            r -= 1
        return grid
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3643 Flip Square Submatrix Vertically -->
