# 1750. Minimum Length of String After Deleting Similar Ends

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Two Pointers` `String`

## Problem

> Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:   	Pick a non-empty prefix from the string s where all the characters in the prefix are equal. 	Pick a non-empty suffix from the string s where all the characters in this suffix are equal. 	The prefix and the suffix should not intersect at any index....

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l < r and s[l] == s[r]:
            chr = s[l]
            while l <= r and s[l] == chr:
                l += 1
            while r >= l and s[r] == chr:
                r -= 1
        return r - l + 1
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1750 Minimum Length of String After Deleting Similar Ends -->
