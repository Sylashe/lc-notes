# 2367. Number of Arithmetic Triplets

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Two Pointers` `Enumeration`

## Problem

> You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:   	i < j < k, 	nums[j] - nums[i] == diff, and 	nums[k] - nums[j] == diff.   Return the number of unique arithmetic triplets.    Example 1:   Input: nums = [0,1,4,6,7,10], diff = 3 Output: 2 Explanation: (1, 2, 4) is an arit...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        i = 0
        j = 1
        for x in nums:
            while diff + nums[j] < x:
                j += 1
            if nums[j] + diff > x:
                continue
            while nums[i] + diff < nums[j]:
                i += 1
            if nums[i] + diff == nums[j]:
                ans += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2367 Number of Arithmetic Triplets -->
