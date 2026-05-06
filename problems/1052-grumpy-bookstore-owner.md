# 1052. Grumpy Bookstore Owner

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Sliding Window`

## Problem

> There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.  During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the b...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = 0
        for i, x in enumerate(customers):
            if not grumpy[i]:
                s += x
        ans = 0
        cnt = 0
        for i, customer in enumerate(customers):
            if grumpy[i]:
                cnt += customer
            if i - minutes + 1 < 0:
                continue
            ans = max(ans, cnt)
            if grumpy[i - minutes + 1]:
                cnt -= customers[i - minutes + 1]
        return ans + s
```

## Complexity

- Time: O()
- Space: O()

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1052 Grumpy Bookstore Owner -->
