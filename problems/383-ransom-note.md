# 383. Ransom Note

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Hash Table` `String` `Counting`

## Problem

> Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.  Each letter in magazine can only be used once in ransomNote.    Example 1: Input: ransomNote = "a", magazine = "b" Output: false Example 2: Input: ransomNote = "aa", magazine = "ab" Output: false Example 3: Input: ransomNote = "aa", magazine = "aab" Outpu...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_ransom = Counter(ransomNote)
        cnt_magazine = Counter(magazine)
        for c in ransomNote:
            if c not in magazine:
                return False
            if cnt_magazine[c] < cnt_ransom[c]:
                return False
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #383 Ransom Note -->
