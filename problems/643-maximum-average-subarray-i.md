# 643. Maximum Average Subarray I

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Sliding Window`

## Problem

> You are given an integer array nums consisting of n elements, and an integer k.  Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.    Example 1:   Input: nums = [1,12,-5,-6,50,3], k = 4 Output: 12.75000 Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 1...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
# 请选择 Python3 提交代码，而不是 Python（即 Python2），后者已经被淘汰了
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_s = -inf  # 窗口元素和的最大值
        s = 0  # 维护窗口元素和
        for i, x in enumerate(nums):
            # 1. 进入窗口
            s += x
            if i < k - 1:  # 窗口大小不足 k
                continue
            # 2. 更新答案
            max_s = max(max_s, s)
            # 3. 离开窗口
            s -= nums[i - k + 1]
        return max_s / k
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #643 Maximum Average Subarray I -->
