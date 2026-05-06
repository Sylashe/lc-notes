# 2300. Successful Pairs of Spells and Potions

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `Binary Search` `Sorting`

## Problem

> You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.  You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.  Return an integer array pairs of length n wher...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        for i in range(len(spells)):
            l = 0
            r = len(potions) - 1
            while l <= r:
                m = l + (r - l) // 2
                if potions[m] * spells[i] < success:
                    l = m + 1
                else:
                    r = m - 1
            ans.append(len(potions) - l)
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2300 Successful Pairs of Spells and Potions -->
