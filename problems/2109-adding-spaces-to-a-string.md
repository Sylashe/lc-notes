# 2109. Adding Spaces to a String

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Two Pointers` `String` `Simulation`

## Problem

> You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.   	For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee"...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l = 0
        ans = []
        for r, c in enumerate(s):
            if l < len(spaces) and r == spaces[l]:
                ans.append(" ")
                ans.append(c)
                l += 1
            else:
                ans.append(c)
        return "".join(ans)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2109 Adding Spaces to a String -->
