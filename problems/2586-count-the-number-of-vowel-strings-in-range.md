# 2586. Count the Number of Vowel Strings in Range

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `String` `Counting`

## Problem

> You are given a 0-indexed array of string words and two integers left and right.  A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.  Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].    Example 1:   Input: words = ["are","amy","u"], left = 0, r...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        cnt = 0
        for i in range(left,right + 1):
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                cnt +=1
        return cnt
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2586 Count the Number of Vowel Strings in Range -->
