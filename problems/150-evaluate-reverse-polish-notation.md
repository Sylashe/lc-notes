# 150. Evaluate Reverse Polish Notation

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Math` `Stack`

## Problem

> You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.  Evaluate the expression. Return an integer that represents the value of the expression.  Note that:   	The valid operators are '+', '-', '*', and '/'. 	Each operand may be an integer or another expression. 	The division between two integers always truncates toward zero. 	There will not...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        operants = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operants:
                num.append(int(token))
            else:
                num2 = int(num.pop())
                num1 = int(num.pop())
                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num1 - num2
                elif token == "*":
                    res = num1 * num2
                else:
                    res = int(num1 / num2)
                num.append(res)
        return num.pop()
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #150 Evaluate Reverse Polish Notation -->
