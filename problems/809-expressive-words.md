# 809. Expressive Words

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `String`

## Problem

> Sometimes people repeat letters to represent extra feeling. For example:   	"hello" -> "heeellooo" 	"hi" -> "hiiii"   In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".  You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the foll...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def check(s, word):
            i = 0
            j = 0
            n = len(s)
            m = len(word)
            while i < n and j < m:
                if s[i] != word[j]:
                    return False
                start_i = i
                while i < n and s[i] == s[start_i]:
                    i += 1
                GroupS = i - start_i
                start_j = j
                while j < m and word[j] == word[start_j]:
                    j += 1
                GroupWord = j - start_j
                if GroupS < 3:
                    if GroupS != GroupWord:
                        return False
                else:
                    if GroupS < GroupWord:
                        return False
            return (i == n and j == m)
        ans = 0
        for word in words:
            if check(s, word):
                ans += 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #809 Expressive Words -->
