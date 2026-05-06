# 409. Longest Palindrome

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Hash Table` `String` `Greedy`

## Problem

> Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.  Letters are case sensitive, for example, "Aa" is not considered a palindrome.    Example 1:   Input: s = "abccccdd" Output: 7 Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.   Example 2:   Input: s = "a" Output:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        check = 0
        for c in cnt:
            if cnt[c] % 2 == 0:
                ans += cnt[c]
            else:
                if check == 0:
                    check += 1
                ans += cnt[c] - 1
        return ans + 1 if check != 0 else ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #409 Longest Palindrome -->
