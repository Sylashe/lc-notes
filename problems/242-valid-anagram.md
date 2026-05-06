# 242. Valid Anagram

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Hash Table` `String` `Sorting`

## Problem

> Given two strings s and t, return true if t is an anagram of s, and false otherwise.    Example 1:   Input: s = "anagram", t = "nagaram"  Output: true   Example 2:   Input: s = "rat", t = "car"  Output: false     Constraints:   	1 <= s.length, t.length <= 5 * 104 	s and t consist of lowercase English letters.     Follow up: What if the inputs contain Unicode characters? How would you adapt your so...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        if len(cnt_s) != len(cnt_t):
            return False
        for element in cnt_s:
            if cnt_s[element] != cnt_t[element]:
                return False
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #242 Valid Anagram -->
