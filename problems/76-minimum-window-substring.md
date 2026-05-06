# 76. Minimum Window Substring

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Hash Table` `String` `Sliding Window`

## Problem

> Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".  The testcases will be generated such that the answer is unique.    Example 1:   Input: s = "ADOBECODEBANC", t = "ABC" Output: "BANC" Explanation: The minimum w...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = defaultdict(int)
        cnt_t = Counter(t)
        valid = 0
        ans = s + '^'
        l = 0
        required = len(cnt_t)
        
        for r, c in enumerate(s):
            if c in cnt_t:
                cnt_s[c] += 1
                if cnt_s[c] == cnt_t[c]:
                    valid += 1
            
            while valid == required:
                if r - l + 1 < len(ans):
                    ans = s[l:r+1]
                
                left_c = s[l]
                if left_c in cnt_t:
                    if cnt_s[left_c] == cnt_t[left_c]:
                        valid -= 1
                    cnt_s[left_c] -= 1
                l += 1
        
        return ans if ans[-1] != '^' else ""
```

## Complexity

- Time: O()
- Space: O()

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #76 Minimum Window Substring -->
