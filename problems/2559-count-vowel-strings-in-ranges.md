# 2559. Count Vowel Strings in Ranges

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `String` `Prefix Sum`

## Problem

> You are given a 0-indexed array of strings words and a 2D array of integers queries.  Each query queries[i] = [li, ri] asks us to find the number of strings present at the indices ranging from li to ri (both inclusive) of words that start and end with a vowel.  Return an array ans of size queries.length, where ans[i] is the answer to the ith query.  Note that the vowel letters are 'a', 'e', 'i', '...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = ['a', 'e', 'i', 'o', 'u']
        pre_sum = [0] * (len(words) + 1)
        ans = []
        for i, word in enumerate(words):
            if word[0] in vowel and word[-1] in vowel:
                pre_sum[i + 1] = pre_sum[i] + 1
            else:
                pre_sum[i + 1] = pre_sum[i]
        for i, query in enumerate(queries):
            l = query[0]
            r = query[1]
            ans.append(pre_sum[r + 1] - pre_sum[l])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2559 Count Vowel Strings in Ranges -->
