# 560. Subarray Sum Equals K

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Prefix Sum`

## Problem

> Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.  A subarray is a contiguous non-empty sequence of elements within an array.    Example 1: Input: nums = [1,1,1], k = 2 Output: 2 Example 2: Input: nums = [1,2,3], k = 3 Output: 2    Constraints:   	1 <= nums.length <= 2 * 104 	-1000 <= nums[i] <= 1000 	-107 <= k <= 107

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        pre_s = 0
        for num in nums:
            pre_s += num
            ans += cnt[pre_s - k]
            cnt[pre_s] += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #560 Subarray Sum Equals K -->
