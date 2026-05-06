# 13. Roman to Integer

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Hash Table` `Math` `String`

## Problem

> Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.   Symbol       Value I             1 V             5 X             10 L             50 C             100 D             500 M             1000  For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX +...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and mp[s[i]] < mp[s[i + 1]]:
                ans -= mp[s[i]]
            else:
                ans += mp[s[i]]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #13 Roman to Integer -->
