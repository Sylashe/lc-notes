# 3379. Transformed Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Simulation`

## Problem

> You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules: For each index i (where 0 <= i < nums.length), perform the following independent actions:   	If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value at the index where you land. 	If nu...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_nums = [0] * n  # 初始化结果数组
        for i in range(n):
            value = nums[i]
            if value > 0:
                # 向右移动 value 步
                new_i = (i + value) % n
            elif value < 0:
                # 向左移动 abs(value) 步
                new_i = (i + value) % n  # Python 的负数取模会自动处理循环
            else:
                # value == 0
                new_i = i
            new_nums[i] = nums[new_i]  # 将 nums[new_i] 的值赋给 new_nums[i]
        return new_nums
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3379 Transformed Array -->
