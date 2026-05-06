# 9. Palindrome Number

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Math`

## Problem

> Given an integer x, return true if x is a palindrome, and false otherwise.    Example 1:   Input: x = 121 Output: true Explanation: 121 reads as 121 from left to right and from right to left.   Example 2:   Input: x = -121 Output: false Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.   Example 3:   Input: x = 10 Output: false E...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse_half = 0
        while x > reverse_half:
            reverse_half = reverse_half * 10 + x % 10
            x //= 10
        return reverse_half == x or reverse_half //10 == x
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #9 Palindrome Number -->
