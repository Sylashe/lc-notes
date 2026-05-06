# 796. Rotate String

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String` `String Matching`

## Problem

> Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.  A shift on s consists of moving the leftmost character of s to the rightmost position.   	For example, if s = "abcde", then it will be "bcdea" after one shift.     Example 1: Input: s = "abcde", goal = "cdeab" Output: true Example 2: Input: s = "abcde", goal = "abced" Output: false    Cons...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s + s
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #796 Rotate String -->
