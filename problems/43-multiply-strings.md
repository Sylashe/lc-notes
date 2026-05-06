# 43. Multiply Strings

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Math` `String` `Simulation`

## Problem

> Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.  Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.    Example 1: Input: num1 = "2", num2 = "3" Output: "6" Example 2: Input: num1 = "123", num2 = "456" Output: "56088"    Constraints:   	1 <= num1.length, num2.lengt...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n = len(num1)
        m = len(num2)
        ans = [0] * (n + m)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                res = mul + ans[i + j + 1]
                carry = res // 10
                digit = res % 10
                ans[i + j + 1] = digit
                ans[i + j] += carry
        idx = 0
        while idx < len(ans) and ans[idx] == 0:
            idx += 1
        s = ''
        while idx < len(ans):
            s += str(ans[idx])
            idx += 1
        return s
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #43 Multiply Strings -->
