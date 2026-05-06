# 522. Longest Uncommon Subsequence II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `Two Pointers` `String` `Sorting`

## Problem

> Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.  An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.  A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.   	For...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(a, b) -> bool:
            j = 0 
            for c in a:
                if c == b[j]:
                    j += 1
                if j == len(b):
                    return True
            return False
        ans = -1
        for i in range(len(strs)):
            s = strs[i]
            ok = True
            for j in range(len(strs)):
                if i == j:
                    continue
                if is_subseq(strs[j], s):
                    ok = False
                    break
            if ok:
                ans = max(ans, len(s))
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #522 Longest Uncommon Subsequence II -->
