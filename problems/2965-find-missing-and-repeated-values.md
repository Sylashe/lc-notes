# 2965. Find Missing and Repeated Values

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Math` `Matrix`

## Problem

> You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.  Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.    Example 1:   Input: grid = [[1,3],[2,2]] Output: [2,4...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n_squared = n * n
        
        expected_sum = n_squared * (n_squared + 1) // 2
        expected_sum_squares = n_squared * (n_squared + 1) * (2 * n_squared + 1) // 6
        
        actual_sum = 0
        actual_sum_squares = 0
        
        for i in range(n):
            for j in range(n):
                actual_sum += grid[i][j]
                actual_sum_squares += grid[i][j] * grid[i][j]

        # a - b
        diff_sum = actual_sum - expected_sum

        # a² - b²
        diff_sum_squares = actual_sum_squares - expected_sum_squares
        
        # a + b = (a² - b²) / (a - b)
        sum_a_b = diff_sum_squares // diff_sum
        
        # Now we can find a and b
        a = (sum_a_b + diff_sum) // 2
        b = (sum_a_b - diff_sum) // 2
        
        return [a, b]
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2965 Find Missing and Repeated Values -->
