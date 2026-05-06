# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Sliding Window`

## Problem

> Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.    Example 1:   Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4 Output: 3 Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold)....

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        s = 0
        for i, num in enumerate(arr):
            s += num
            if i - k + 1 < 0:
                continue
            if s/k >= threshold:
                cnt += 1
            s -= arr[i - k + 1]
        return cnt
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1343 Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold -->
