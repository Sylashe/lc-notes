# 128. Longest Consecutive Sequence

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Union-Find`

## Problem

> Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.  You must write an algorithm that runs in O(n) time.    Example 1:   Input: nums = [100,4,200,1,3,2] Output: 4 Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.   Example 2:   Input: nums = [0,3,7,2,5,8,4,6,0,1] Output: 9   Example 3:   Input: n...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        i = cnt = ans = 0
        while i < len(nums):
            if i == 0 or nums[i] == nums[i - 1] + 1:
                cnt += 1
            else:
                ans = max(cnt, ans)
                cnt = 1
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        ans = max(cnt, ans)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #128 Longest Consecutive Sequence -->
