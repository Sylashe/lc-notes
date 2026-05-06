# 402. Remove K Digits

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String` `Stack` `Greedy` `Monotonic Stack`

## Problem

> Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.    Example 1:   Input: num = "1432219", k = 3 Output: "1219" Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.   Example 2:   Input: num = "10200", k = 1 Output: "200" Explanation: Remove the leading 1 a...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i, x in enumerate(num):
            while stack and k and stack[-1] > x:
                stack.pop()
                k -= 1
            stack.append(x)
        while k > 0:
            stack.pop()
            k -= 1
        stack = ''.join(stack)
        ans = stack.lstrip('0')
        return ans if ans else '0'
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #402 Remove K Digits -->
