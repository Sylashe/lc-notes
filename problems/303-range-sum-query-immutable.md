# 303. Range Sum Query - Immutable

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Design` `Prefix Sum`

## Problem

> Given an integer array nums, handle multiple queries of the following type:   	Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.   Implement the NumArray class:   	NumArray(int[] nums) Initializes the object with the integer array nums. 	int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inc...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class NumArray:

    def __init__(self, nums: List[int]):
        pre_f = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            pre_f[i + 1] = num + pre_f[i]
        self.pre_f = pre_f
    def sumRange(self, left: int, right: int) -> int:
        pre_f = self.pre_f
        return pre_f[right + 1] - pre_f[left]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #303 Range Sum Query - Immutable -->
