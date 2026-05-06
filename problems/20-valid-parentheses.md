# 20. Valid Parentheses

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String` `Stack`

## Problem

> Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.  An input string is valid if:   	Open brackets must be closed by the same type of brackets. 	Open brackets must be closed in the correct order. 	Every close bracket has a corresponding open bracket of the same type.     Example 1:   Input: s = "()"  Output: true   Example 2:   I...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def isValid(self, s: str) -> bool:
        paren_match = {')':'(', ']':'[','}':'{'}
        stack = []
        for i, fuck in enumerate(s):
            if fuck not in paren_match:
                stack.append(fuck)
            else:
                if len(stack) == 0:
                    return False
                if paren_match[fuck] != stack.pop():
                    return False
        return not stack
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #20 Valid Parentheses -->
