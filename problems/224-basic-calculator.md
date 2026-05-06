# 224. Basic Calculator

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Math` `String` `Stack` `Recursion`

## Problem

> Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.  Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().    Example 1:   Input: s = "1 + 1" Output: 2   Example 2:   Input: s = " 2-1 + 2 " Output: 3   Example 3:   Input: s = "(1+(4+5+2)-3)+(6+8)...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def calculate(self, s: str) -> int:
        numStack = []
        signStack = []
        operators = ['+', '-']
        digit = 0
        sign = 1
        res = 0
        for c in s:
            if c == ' ':
                continue
            if c.isdigit():
                digit = digit * 10 + int(c)
            elif c in operators:
                res = res + digit * sign
                digit = 0
                if c == '+':
                    sign = 1
                else:
                    sign = -1
            elif c == '(':
                numStack.append(res)
                signStack.append(sign)
                res = 0
                sign = 1
            else:
                res += sign * digit
                digit = 0
                res = numStack.pop() + res * signStack.pop()
        res += sign * digit
        return res
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #224 Basic Calculator -->
