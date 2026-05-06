# 1385. Find the Distance Value Between Two Arrays

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Two Pointers` `Binary Search` `Sorting`

## Problem

> Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.  The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.    Example 1:   Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2 Output: 2 Explanation:  For arr1[0]=4 we have:  |4-10|=6 > d=2  |4-9|=5 > d=2  |4-1|=3 >...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        '''数值不落在这个区间
        =>-d <= arr1[i] - arr2[j] <= d
        '''

        '''
        所以数值要么落在
        arr1[i] - arr2[j] < -d
        要么落在
        arr1[i] - arr2[j] > d

        arr
        '''

        '''
        因为not any element arr2[j]
        所以应该arr2和arr1之间不需要有数值 
        index对应的需求， 可以排序来优化，因为有
        比大小，所以排序后可以利用这个优化
        '''
        arr1.sort()
        arr2.sort()
        cnt = 0
        j = 0
        for i, num in enumerate(arr1):
            while j < len(arr2) and arr1[i] - arr2[j] > d:
                j += 1
            if j == len(arr2) or arr1[i] - arr2[j] < -d:
                cnt += 1
        return cnt
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #1385 Find the Distance Value Between Two Arrays -->
