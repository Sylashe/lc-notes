# 1839. Longest Substring Of All Vowels in Order

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String` `Sliding Window`

## Problem

> A string is considered beautiful if it satisfies the following conditions:   	Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it. 	The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).   For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not bea...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = "aeiou"
        n = len(word)
        i = 0
        v_i = 0
        cnt = 0
        ans = 0

        while i < n:
            # 已经完成 aeiou（上一段结束），重置去找下一段
            if v_i == 5:
                cnt = 0
                v_i = 0

            # 当前字符不等于期望元音：如果是 'a'，从这里重新开始；否则跳过
            if word[i] != vowels[v_i]:
                if word[i] == 'a':
                    cnt = 0
                    v_i = 0
                    continue
                i += 1
                cnt = 0
                v_i = 0
                continue

            # 吃掉当前期望元音的一整段（连续相同字符）
            while i < n and word[i] == vowels[v_i]:
                i += 1
                cnt += 1

            v_i += 1

            # 刚好完成 aeiou，更新答案
            if v_i == 5:
                ans = max(ans, cnt)

        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1839 Longest Substring Of All Vowels in Order -->
