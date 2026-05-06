# 1422. Maximum Score After Splitting a String

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String` `Prefix Sum`

## Problem

> Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).  The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.    Example 1:   Input: s = "011101" Output: 5  Explanation:  All possible ways of splitting s into two non-emp...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxScore(self, s: str) -> int:
        score = s.count('1')
        ans = 0
        for i in range(0,len(s) - 1):
            if s[i] == '0':
                score += 1
            else:
                score -= 1
            ans = max(ans, score)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1422 Maximum Score After Splitting a String -->
