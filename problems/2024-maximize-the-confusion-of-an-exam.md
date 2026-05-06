# 2024. Maximize the Confusion of an Exam

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `String` `Binary Search` `Sliding Window` `Prefix Sum`

## Problem

> A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).  You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the max...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        ans = 0
        cnt = defaultdict(int)
        for right, c in enumerate(answerKey):
            cnt[c] += 1
            while cnt['T'] > k and cnt['F'] > k:
                cnt[answerKey[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2024 Maximize the Confusion of an Exam -->
