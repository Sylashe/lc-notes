# 567. Permutation in String

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Hash Table` `Two Pointers` `String` `Sliding Window`

## Problem

> Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.  In other words, return true if one of s1's permutations is the substring of s2.    Example 1:   Input: s1 = "ab", s2 = "eidbaooo" Output: true Explanation: s2 contains one permutation of s1 ("ba").   Example 2:   Input: s1 = "ab", s2 = "eidboaoo" Output: false     Constraints:   	1 <= s1.length, s2.le...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt_s1 = Counter(s1)
        cnt_s2 = defaultdict(int)
        k = len(s1)
        valid = 0
        for i, c in enumerate(s2):
            cnt_s2[c] += 1
            if cnt_s2[c] == cnt_s1[c]:
                valid += 1
            if i - k + 1 < 0:
                continue
            if valid == len(cnt_s1):
                return True
            if s2[i - k + 1] in s1:
                if cnt_s2[s2[i - k + 1]] == cnt_s1[s2[i - k + 1]]:
                    valid -= 1
                cnt_s2[s2[i - k + 1]] -= 1
        return False
```

## Complexity

- Time: O()
- Space: O()

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #567 Permutation in String -->
