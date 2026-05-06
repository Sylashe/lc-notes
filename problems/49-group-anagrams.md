# 49. Group Anagrams

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table` `String` `Sorting`

## Problem

> Given an array of strings strs, group the anagrams together. You can return the answer in any order.    Example 1:   Input: strs = ["eat","tea","tan","ate","nat","bat"]  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]  Explanation:   	There is no string in strs that can be rearranged to form "bat". 	The strings "nat" and "tan" are anagrams as they can be rearranged to form each other. 	The str...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            grp[sorted_word].append(word)
        return list(grp.values())
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #49 Group Anagrams -->
