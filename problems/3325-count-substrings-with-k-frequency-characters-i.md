# 3325. Count Substrings With K-Frequency Characters I

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Hash Table` `String` `Sliding Window`

## Problem

> Given a string s and an integer k, return the total number of substrings of s where at least one character appears at least k times.    Example 1:   Input: s = "abacb", k = 2  Output: 4  Explanation:  The valid substrings are:   	"aba" (character 'a' appears 2 times). 	"abac" (character 'a' appears 2 times). 	"abacb" (character 'a' appears 2 times). 	"bacb" (character 'b' appears 2 times).    Exam...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        l = 0
        for r, c in enumerate(s):
            cnt[c] += 1
            while max(cnt.values()) == k:
                cnt[s[l]] -= 1
                l += 1
            ans += l
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3325 Count Substrings With K-Frequency Characters I -->
