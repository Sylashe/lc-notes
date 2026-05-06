# 1091. Shortest Path in Binary Matrix

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Breadth-First Search` `Matrix`

## Problem

> Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.  A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:   	All the visited cells of the path are 0. 	All the adjacent cells of the path are 8-directionally connected (i.e., they are d...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```cpp
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1){
            return -1;
        }


        int dx[8] = {1, 1, 1, 0, 0, -1, -1, -1};
        int dy[8] = {1, 0, -1, 1, -1, 1, 0, -1};


        queue<int> qx;
        queue<int> qy;
        qx.push(0);
        qy.push(0);
        grid[0][0] = 1; 


        while (!qx.empty()) {
            int x = qx.front();
            int y = qy.front();
            qx.pop();
            qy.pop();
            int dist = grid[x][y];
            if (x == n - 1 && y == n - 1){
                return dist;
            }
            for (int i = 0; i < 8; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < n && ny < n && grid[nx][ny] == 0) {
                    grid[nx][ny] = dist + 1;
                    qx.push(nx);
                    qy.push(ny);
                }
            }
        }
        return -1;
    }
};
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1091 Shortest Path in Binary Matrix -->
