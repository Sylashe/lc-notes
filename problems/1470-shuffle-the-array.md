# 1470. Shuffle the Array

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array`

## Problem

> Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].  Return the array in the form [x1,y1,x2,y2,...,xn,yn].    Example 1:   Input: nums = [2,5,1,3,4,7], n = 3 Output: [2,3,5,4,1,7]  Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].   Example 2:   Input: nums = [1,2,3,4,4,3,2,1], n = 4 Output: [1,4,2,3,3,2,4,1...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(0,n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1470 Shuffle the Array -->
