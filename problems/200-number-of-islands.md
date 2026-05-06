# 200. Number of Islands

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Depth-First Search` `Breadth-First Search` `Union-Find` `Matrix`

## Problem

> Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.    Example 1:   Input: grid = [   ["1","1","1","1","0"],   ["1","1","0","1","0"],   ["1","1","0","0","0...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```cpp
class Solution {
public:
    int m, n;
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};


    void helper(vector<vector<char>>& grid, int x, int y){
        if(x < 0 || y < 0 || x >= m || y >= n){
            return;
        }

        if(grid[x][y] != '1'){
            return;
        }

        grid[x][y] = '2';
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            helper(grid, nx, ny);
        }
    }

    int numIslands(vector<vector<char>>& grid){
        m = grid.size();
        n = grid[0].size();
        int count = 0;
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == '1'){
                    helper(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }
};
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #200 Number of Islands -->
