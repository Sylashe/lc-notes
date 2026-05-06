# 1310. XOR Queries of a Subarray

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Bit Manipulation` `Prefix Sum`

## Problem

> You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].  For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).  Return an array answer where answer[i] is the answer to the ith query.    Example 1:   Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_sum = [0] * (len(arr) + 1)
        ans = []
        for i, num in enumerate(arr):
            pre_sum[i + 1] = pre_sum[i] ^ num
        for _, query in enumerate(queries):
            l = query[0]
            r = query[1]
            ans.append(pre_sum[r + 1] ^ pre_sum[l])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1310 XOR Queries of a Subarray -->
