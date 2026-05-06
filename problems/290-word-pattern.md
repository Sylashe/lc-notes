# 290. Word Pattern

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Hash Table` `String`

## Problem

> Given a pattern and a string s, find if s follows the same pattern.  Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:   	Each letter in pattern maps to exactly one unique word in s. 	Each unique word in s maps to exactly one letter in pattern. 	No two letters map to the same word, and no two words map to the same le...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = dict()
        s = s.split()
        seen = set()
        if not len(s) == len(pattern):
            return False
        for i, word in enumerate(s):
            if pattern[i] not in mp:
                if word not in seen:
                    mp[pattern[i]] = word
                    seen.add(word)
                else:
                    return False
            else:
                if mp[pattern[i]] != word:
                    return False
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #290 Word Pattern -->
