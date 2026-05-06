# 239. Sliding Window Maximum

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Array` `Queue` `Sliding Window` `Heap (Priority Queue)` `Monotonic Queue`

## Problem

> You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.  Return the max sliding window.    Example 1:   Input: nums = [1,3,-1,-3,5,3,6,7], k = 3 Output: [3,3,5,5,6,7] Explanation:  Window position...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * (len(nums) - k + 1)
        q = deque()
        for i, num in enumerate(nums):
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(i)
            window_head = i - k + 1
            if q[0] < window_head:
                q.popleft()
            if window_head >= 0:
                ans[window_head] = nums[q[0]]
        return ans
```

## Complexity

- Time: O()
- Space: O()

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #239 Sliding Window Maximum -->
