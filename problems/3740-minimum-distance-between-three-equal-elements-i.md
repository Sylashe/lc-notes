# 3740. Minimum Distance Between Three Equal Elements I

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table`

## Problem

> You are given an integer array nums.  A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].  The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.  Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.    Example 1:   Input: nums = [1,2,1,1,3]  Output: 6...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        print(pos)
        for i, x in enumerate(nums):
            pos[x].append(i)
        ans = inf
        for val_ in pos.values():
            for i in range(2, len(val_)):
                ans = min(ans, (val_[i] - val_[i - 2]) * 2)
        return -1 if ans == inf else ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3740 Minimum Distance Between Three Equal Elements I -->
