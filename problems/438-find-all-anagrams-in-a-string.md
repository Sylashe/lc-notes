# 438. Find All Anagrams in a String

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Hash Table` `String` `Sliding Window`

## Problem

> Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.    Example 1:   Input: s = "cbaebabacd", p = "abc" Output: [0,6] Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc". The substring with start index = 6 is "bac", which is an anagram of "abc".   Example 2:   Input: s = "abab", p = "ab"...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        cnt_s = defaultdict(int)
        cnt_p = Counter(p)
        ans = []
        valid = 0
        for i, c in enumerate(s):
            cnt_s[c] += 1
            if cnt_s[c] == cnt_p[c]:
                valid += 1
            if i - k + 1 < 0:
                continue
            if valid == len(cnt_p):
                ans.append(i - k + 1)
            if s[i - k + 1] in cnt_p:
                if cnt_s[s[i - k + 1]] == cnt_p[s[i - k + 1]]:
                    valid -= 1
            cnt_s[s[i - k + 1]] -= 1
        return ans
```

## Complexity

- Time: O()
- Space: O()

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #438 Find All Anagrams in a String -->
