# 219. Contains Duplicate II

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Sliding Window`

## Problem

> Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.    Example 1:   Input: nums = [1,2,3,1], k = 3 Output: true   Example 2:   Input: nums = [1,0,1,1], k = 1 Output: true   Example 3:   Input: nums = [1,2,3,1,2,3], k = 2 Output: false     Constraints:   	1 <= nums.length <= 105 	-109 <= n...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = dict()
        for i, num in enumerate(nums):
            if num in mp and abs(i - mp[num]) <= k:
                return True
            else:
                mp[num] = i
        return False
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #219 Contains Duplicate II -->
