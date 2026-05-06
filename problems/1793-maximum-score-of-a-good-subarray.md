# 1793. Maximum Score of a Good Subarray

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Array` `Two Pointers` `Binary Search` `Stack` `Monotonic Stack`

## Problem

> You are given an array of integers nums (0-indexed) and an integer k.  The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.  Return the maximum possible score of a good subarray.    Example 1:   Input: nums = [1,4,3,7,4,5], k = 3 Output: 15 Explanation: The optimal subarray is (1, 5) with a score of min(4...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        min_num = nums[k]
        ans = min_num
        n = len(nums)
        for _ in range(n - 1):
            if r == n - 1 or l >= 1 and nums[l - 1] >= nums[r + 1]:
                l -= 1
                min_num = min(min_num, nums[l])
            else:
                r += 1
                min_num = min(min_num, nums[r])
            score = min_num * (r - l + 1)
            ans = max(ans, score)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1793 Maximum Score of a Good Subarray -->
