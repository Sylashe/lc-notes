# 304. Range Sum Query 2D - Immutable

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Design` `Matrix` `Prefix Sum`

## Problem

> Given a 2D matrix matrix, handle multiple queries of the following type:   	Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).   Implement the NumMatrix class:   	NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix. 	int sumRegion(int row1, int col1, int row2, int col2) Retu...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = list(matrix)
        n, m = len(matrix[0]), len(matrix)
        self.pre_s = [(n + 1) * [0] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.pre_s[i + 1][j + 1] = self.pre_s[i + 1][j] + self.pre_s[i][j + 1] - self.pre_s[i][j] + matrix[i][j]

        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pre_s = self.pre_s
        a, b = row1, col1
        c, d = row2, col2
        return pre_s[c + 1][d + 1] - pre_s[c + 1][b] - pre_s[a][d + 1] + pre_s[a][b]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #304 Range Sum Query 2D - Immutable -->
