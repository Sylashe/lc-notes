# 1869. Longer Contiguous Segments of Ones than Zeros

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `String`

## Problem

> Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.   	For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.   Note that if there are no 0's, then the longest continuous segment of 0's is conside...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        def longest_k_element(s, k) -> int:
            if s[0] == k:
                ans = 1
                cnt = 1
            else:
                ans = 0
                cnt = 0
            for i in range(1, len(s)):
                if s[i] == k:
                    cnt += 1
                else:
                    cnt = 0
                ans = max(ans, cnt)
            return ans 
        return longest_k_element(s, "1") > longest_k_element(s, "0")
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1869 Longer Contiguous Segments of Ones than Zeros -->
