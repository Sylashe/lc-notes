# 2. Add Two Numbers

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Linked List` `Math` `Recursion`

## Problem

> You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.  You may assume the two numbers do not contain any leading zero, except the number 0 itself.    Example 1:   Input: l1 = [2,4,3], l2 = [5,6,4] Output: [7,0,8] Explanation: 3...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = ListNode(0)
        dummy.next = head
        h1 = l1
        h2 = l2
        carry = 0
        while h1 or h2 or carry:
            if h1:
                val1 = h1.val
                h1 = h1.next
            else:
                val1 = 0
            if h2:
                val2 = h2.val
                h2 = h2.next
            else:
                val2 = 0
            total = val1 + val2
            head.next = ListNode((total + carry) % 10)
            carry = (total + carry) // 10
            head = head.next
        return dummy.next.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #2 Add Two Numbers -->
