# 24. Swap Nodes in Pairs

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Linked List` `Recursion`

## Problem

> Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)    Example 1:   Input: head = [1,2,3,4]  Output: [2,1,4,3]  Explanation:     Example 2:   Input: head = []  Output: []   Example 3:   Input: head = [1]  Output: [1]   Example 4:   Input: head = [1,2,3]  Out...

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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head != None and head.next != None:
            first = head
            second = first.next
            third = second.next

            second.next = first
            first.next = third
            prev.next = second

            prev = first
            head = third
        return dummy.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #24 Swap Nodes in Pairs -->
