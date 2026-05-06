# 3090. Maximum Length Substring With Two Occurrences

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Hash Table` `String` `Sliding Window`

## Problem

> Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.   Example 1:   Input: s = "bcbbbcba"  Output: 4  Explanation: The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".  Example 2:   Input: s = "aaaa"  Output: 2  Explanation: The following substring has a length of 2 and c...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = Counter()
        l = 0
        ans = 0
        for r, char in enumerate(s):
            cnt[char] += 1
            while cnt[s[r]] > 2:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3090 Maximum Length Substring With Two Occurrences -->
