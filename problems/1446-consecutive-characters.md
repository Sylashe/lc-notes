# 1446. Consecutive Characters

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String`

## Problem

> The power of the string is the maximum length of a non-empty substring that contains only one unique character.  Given a string s, return the power of s.    Example 1:   Input: s = "leetcode" Output: 2 Explanation: The substring "ee" is of length 2 with the character 'e' only.   Example 2:   Input: s = "abbcccddddeeeeedcba" Output: 5 Explanation: The substring "eeeee" is of length 5 with the chara...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1446 Consecutive Characters -->
