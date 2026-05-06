# 1456. Maximum Number of Vowels in a Substring of Given Length

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String` `Sliding Window`

## Problem

> Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.  Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.    Example 1:   Input: s = "abciiidef", k = 3 Output: 3 Explanation: The substring "iii" contains 3 vowel letters.   Example 2:   Input: s = "aeiou", k = 2 Output: 2 Explanation: Any substring of length 2 contains 2 vowels....

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = 'aeiou'
        ans = 0
        cnt = 0
        for i, c in enumerate(s):
            if c in vowel:
                cnt += 1
            if i - k + 1 < 0:
                continue
            ans = max(ans, cnt)
            if s[i - k + 1] in vowel:
                cnt -= 1
        return ans
```

## Complexity

- Time: O()
- Space: O()

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1456 Maximum Number of Vowels in a Substring of Given Length -->
