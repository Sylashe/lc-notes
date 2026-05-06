# 2273. Find Resultant Array After Removing Anagrams

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Hash Table` `String` `Sorting`

## Problem

> You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.  In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.  Return words after performing all operations. It can be s...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            if Counter(words[i]) == Counter(words[i - 1]):
                del words[i]
            else:
                i += 1
        return words
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2273 Find Resultant Array After Removing Anagrams -->
