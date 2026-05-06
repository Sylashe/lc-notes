# 860. Lemonade Change

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Array` `Greedy`

## Problem

> At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.  Note that you do not have any change in hand at f...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:  
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                ten += 1
                five -= 1
            else:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #860 Lemonade Change -->
