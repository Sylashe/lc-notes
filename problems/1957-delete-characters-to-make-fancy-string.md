# 1957. Delete Characters to Make Fancy String

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String`

## Problem

> A fancy string is a string where no three consecutive characters are equal.  Given a string s, delete the minimum possible number of characters from s to make it fancy.  Return the final string after the deletion. It can be shown that the answer will always be unique.    Example 1:   Input: s = "leeetcode" Output: "leetcode" Explanation: Remove an 'e' from the first group of 'e's to create "leetco...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def makeFancyString(self, s: str) -> str:
        cnt = 0
        ans = ""
        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                ans += s[i]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1957 Delete Characters to Make Fancy String -->
