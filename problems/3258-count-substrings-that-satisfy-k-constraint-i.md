# 3258. Count Substrings That Satisfy K-Constraint I

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String` `Sliding Window`

## Problem

> You are given a binary string s and an integer k.  A binary string satisfies the k-constraint if either of the following conditions holds:   	The number of 0's in the string is at most k. 	The number of 1's in the string is at most k.   Return an integer denoting the number of substrings of s that satisfy the k-constraint.    Example 1:   Input: s = "10101", k = 1  Output: 12  Explanation:  Every...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        l = ans = 0
        for r,num in enumerate(s):
            cnt[num] += 1
            while cnt['0'] > k and cnt['1'] > k:
                cnt[s[l]] -= 1
                l += 1
            ans += r - l + 1
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3258 Count Substrings That Satisfy K-Constraint I -->
