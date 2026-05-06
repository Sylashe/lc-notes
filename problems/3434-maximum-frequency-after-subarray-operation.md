# 3434. Maximum Frequency After Subarray Operation

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Dynamic Programming` `Greedy` `Enumeration` `Prefix Sum`

## Problem

> You are given an array nums of length n. You are also given an integer k.  You perform the following operation on nums once:   	Select a subarray nums[i..j] where 0 <= i <= j <= n - 1. 	Select an integer x and add x to all the elements in nums[i..j].   Find the maximum frequency of the value k after the operation.    Example 1:   Input: nums = [1,2,3,4,5,6], k = 1  Output: 2  Explanation:  After a...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        original_k = nums.count(k)
        max_gain = 0
        for v in range(1, 51):
            if v == k:
                continue  
            current_max = 0
            max_subarray = 0
            for num in nums:
                if num == v:
                    diff = 1
                elif num == k:
                    diff = -1
                else:
                    diff = 0
                current_max = max(diff, current_max + diff)
                max_subarray = max(max_subarray, current_max)
            if max_subarray > max_gain:
                max_gain = max_subarray
        result = original_k + max_gain
        return max(result, original_k)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3434 Maximum Frequency After Subarray Operation -->
