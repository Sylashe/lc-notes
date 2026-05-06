# 3. Longest Substring Without Repeating Characters

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Hash Table` `String` `Sliding Window`

## Problem

> Given a string s, find the length of the longest substring without duplicate characters.    Example 1:   Input: s = "abcabcbb" Output: 3 Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.   Example 2:   Input: s = "bbbbb" Output: 1 Explanation: The answer is "b", with the length of 1.   Example 3:   Input: s = "pwwkew" Output: 3 Explanation:...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = set()
        l = 0
        ans = 0
        for i, c in enumerate(s):
            while c in cnt:
                cnt.remove(s[l])
                l += 1
            cnt.add(c)
            ans = max(ans, i - l + 1)
        return ans
```

## Complexity

- Time: O()
- Space: O()

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3 Longest Substring Without Repeating Characters -->
