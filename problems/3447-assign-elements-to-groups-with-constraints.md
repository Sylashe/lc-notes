# 3447. Assign Elements to Groups with Constraints

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Array` `Hash Table`

## Problem

> You are given an integer array groups, where groups[i] represents the size of the ith group. You are also given an integer array elements.  Your task is to assign one element to each group based on the following rules:   	An element at index j can be assigned to a group i if groups[i] is divisible by elements[j]. 	If there are multiple elements that can be assigned, assign the element with the sma...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        mx = max(groups)
        target = [-1] * (mx + 1)
        for i, ele in enumerate(elements):
            if ele > mx or target[ele] != -1:
                continue
            for y in range(ele, mx + 1, ele):
                if target[y] == -1:
                    target[y] = i
        ans = []
        for x in (groups):
            ans.append(target[x])
        return ans
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #3447 Assign Elements to Groups with Constraints -->
