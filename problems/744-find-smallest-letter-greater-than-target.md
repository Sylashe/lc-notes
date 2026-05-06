# 744. Find Smallest Letter Greater Than Target

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Binary Search`

## Problem

> You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.  Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.    Example 1:   Input: letters = ["c","f","j"], target = "a" Output: "c...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return letters[l] if l < len(letters) else letters[0]
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #744 Find Smallest Letter Greater Than Target -->
