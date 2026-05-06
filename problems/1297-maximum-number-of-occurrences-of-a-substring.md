# 1297. Maximum Number of Occurrences of a Substring

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Hash Table` `String` `Sliding Window`

## Problem

> Given a string s, return the maximum number of occurrences of any substring under the following rules:   	The number of unique characters in the substring must be less than or equal to maxLetters. 	The substring size must be between minSize and maxSize inclusive.     Example 1:   Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4 Output: 2 Explanation: Substring "aab" has 2 occurrenc...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        ans = 0
        cnt = Counter(s[:minSize])
        sub_cnt = Counter()
        for i in range(n - minSize + 1):
            subString = s[i:minSize + i]
            if len(cnt) <= maxLetters:
                sub_cnt[subString] += 1
                ans = max(ans,sub_cnt[subString])
            if i + minSize < n:
                cnt[s[i]] -= 1
                cnt[s[minSize + i]] += 1
            if cnt[s[i]] == 0:
                del cnt[s[i]]
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1297 Maximum Number of Occurrences of a Substring -->
