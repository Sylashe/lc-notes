# 169. Majority Element

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `Divide and Conquer` `Sorting` `Counting`

## Problem

> Given an array nums of size n, return the majority element.  The majority element is the element that appears more than &lfloor;n / 2&rfloor; times. You may assume that the majority element always exists in the array.    Example 1: Input: nums = [3,2,3] Output: 3 Example 2: Input: nums = [2,2,1,1,1,2,2] Output: 2    Constraints:   	n == nums.length 	1 <= n <= 5 * 104 	-109 <= nums[i] <= 109 	The i...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if cnt == 0:
                ans = nums[i]
                cnt = 1
                continue
            if nums[i] == ans:
                cnt += 1
            else:
                cnt -= 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #169 Majority Element -->
