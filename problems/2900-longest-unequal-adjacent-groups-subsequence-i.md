# 2900. Longest Unequal Adjacent Groups Subsequence I

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `String` `Dynamic Programming` `Greedy`

## Problem

> You are given a string array words and a binary array groups both of length n.  A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements at the same indices in groups are different (that is, there cannot be consecutive 0 or 1).  Your task is to select the longest alternating subsequence from words.  Return the selected subsequence. If t...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        for i, num in enumerate(groups):
            if i == len(groups) - 1 or num != groups[i + 1]:
                ans.append(words[i])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2900 Longest Unequal Adjacent Groups Subsequence I -->
