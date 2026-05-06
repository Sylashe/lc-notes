# 387. First Unique Character in a String

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Hash Table` `String` `Queue` `Counting`

## Problem

> Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.    Example 1:   Input: s = "leetcode"  Output: 0  Explanation:  The character 'l' at index 0 is the first character that does not occur at any other index.   Example 2:   Input: s = "loveleetcode"  Output: 2   Example 3:   Input: s = "aabb"  Output: -1     Constraints:   	1 <= s.le...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #387 First Unique Character in a String -->
