# 3684. Maximize Sum of At Most K Distinct Elements

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Greedy` `Sorting`

## Problem

> You are given a positive integer array nums and an integer k.  Choose at most k elements from nums so that their sum is maximized. However, the chosen numbers must be distinct.  Return an array containing the chosen numbers in strictly descending order.    Example 1:   Input: nums = [84,93,100,77,90], k = 3  Output: [100,93,90]  Explanation:  The maximum sum is 283, which is attained by choosing 9...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = set(nums)
        nums = sorted(nums)
        nums = nums[::-1]
        return nums[:k] if len(nums) > k else nums
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3684 Maximize Sum of At Most K Distinct Elements -->
