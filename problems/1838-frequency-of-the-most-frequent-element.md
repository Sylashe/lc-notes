# 1838. Frequency of the Most Frequent Element

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Binary Search` `Greedy` `Sliding Window` `Sorting` `Prefix Sum`

## Problem

> The frequency of an element is the number of times it occurs in an array.  You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.  Return the maximum possible frequency of an element after performing at most k operations.    Example 1:   Input: nums = [1,2,4], k = 5 Output: 3 Explanation: Increment the f...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        l = 0
        s = 0
        ans = 0
        for r,num in enumerate(nums):
            s += num
            while nums[r]*(r-l+1) - s>k:
                s -= nums[l]
                l += 1
            ans = max(ans,r-l+1)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1838 Frequency of the Most Frequent Element -->
