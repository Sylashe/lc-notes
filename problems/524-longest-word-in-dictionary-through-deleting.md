# 524. Longest Word in Dictionary through Deleting

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `String` `Sorting`

## Problem

> Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.    Example 1:   Input: s = "abpcplea", dictionary = ["ale","apple","monkey"...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def check(s, word):
            i = j = 0
            n = len(s)
            m = len(word)
            while i < n and j < m:
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == m
        cnt = 0
        ans = ""
        for word in dictionary:
            if check(s, word):
                if len(word) > cnt:
                    cnt = len(word)
                    ans = word
                elif len(word) == cnt and word < ans:
                    ans = word
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #524 Longest Word in Dictionary through Deleting -->
