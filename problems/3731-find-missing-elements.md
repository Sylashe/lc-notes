# 3731. Find Missing Elements

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Sorting`

## Problem

> You are given an integer array nums consisting of unique integers.  Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.  The smallest and largest integers of the original range are still present in nums.  Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.    Ex...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        mx = max(nums)
        mn = min(nums)
        i = 0
        for num in range(mn, mx + 1):
            if num == nums[i]:
                i += 1
            else:
                ans.append(num)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3731 Find Missing Elements -->
