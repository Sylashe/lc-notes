# 3298. Count Substrings That Can Be Rearranged to Contain a String II

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Hash Table` `String` `Sliding Window`

## Problem

> You are given two strings word1 and word2.  A string x is called valid if x can be rearranged to have word2 as a prefix.  Return the total number of valid substrings of word1.  Note that the memory limits in this problem are smaller than usual, so you must implement a solution with a linear runtime complexity.    Example 1:   Input: word1 = "bcca", word2 = "abc"  Output: 1  Explanation:  The only...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        cnt = defaultdict(int)
        for c in word2:
            cnt[c] += 1
        diff = len(cnt)
        ans = 0
        l = 0
        for r, c in enumerate(word1):
            cnt[c] -= 1
            if cnt[c] == 0:
                diff -= 1
            while diff == 0:
                if cnt[word1[l]] == 0:
                    diff += 1
                cnt[word1[l]] += 1
                l += 1
            ans += l
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3298 Count Substrings That Can Be Rearranged to Contain a String II -->
