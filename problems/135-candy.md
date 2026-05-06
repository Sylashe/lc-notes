# 135. Candy

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Array` `Greedy`

## Problem

> There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.  You are giving candies to these children subjected to the following requirements:   	Each child must have at least one candy. 	Children with a higher rating get more candies than their neighbors.   Return the minimum number of candies you need to have to distribute the candies to the...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = n * [1]
        for i in range(n):
            if i == 0:
                continue
            if ratings[i] > ratings[i - 1]:
                ans[i] = ans[i - 1] + 1
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                continue
            if ratings[i] > ratings[i + 1]:
                ans[i] =max(ans[i], ans[i + 1] + 1)
        return sum(ans)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #135 Candy -->
