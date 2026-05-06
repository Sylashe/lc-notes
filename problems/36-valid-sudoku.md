# 36. Valid Sudoku

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Matrix`

## Problem

> Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:   	Each row must contain the digits 1-9 without repetition. 	Each column must contain the digits 1-9 without repetition. 	Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.   Note:   	A Sudoku board (partially filled) could be valid but...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_has = [[False] * 9 for _ in range(9)]
        col_has = [[False] * 9 for _ in range(9)]
        sub_box_has = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == '.':
                    continue
                v = int(v) - 1
                if row_has[i][v] or col_has[j][v] or sub_box_has[i//3][j//3][v]:
                    return False
                row_has[i][v] = col_has[j][v] = sub_box_has[i//3][j//3][v] = True
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #36 Valid Sudoku -->
