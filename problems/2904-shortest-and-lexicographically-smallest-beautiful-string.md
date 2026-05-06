# 2904. Shortest and Lexicographically Smallest Beautiful String

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String` `Sliding Window`

## Problem

> You are given a binary string s and a positive integer k.  A substring of s is beautiful if the number of 1's in it is exactly k.  Let len be the length of the shortest beautiful substring.  Return the lexicographically smallest beautiful substring of string s with length equal to len. If s doesn't contain a beautiful substring, return an empty string.  A string a is lexicographically larger than...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ''
        ans = s
        left = 0
        cnt_1 = 0
        for right, c in enumerate(s):
            cnt_1 += int(c)
            while cnt_1 > k or s[left] == '0':
                cnt_1 -= int(s[left])
                left += 1
            if cnt_1 == k:
                p = s[left:right + 1]
                if len(p) < len(ans) or len(p) == len(ans) and p < ans:
                    ans = p
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2904 Shortest and Lexicographically Smallest Beautiful String -->
