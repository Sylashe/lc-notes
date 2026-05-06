# 142. Linked List Cycle II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Hash Table` `Linked List` `Two Pointers`

## Problem

> Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.  There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that po...

## Key Insight

<!-- What clicked / what you kept missing -->

## Approach

<!-- Step-by-step breakdown -->

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != head:
                    slow = slow.next
                    head = head.next
                return head
        return None
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #142 Linked List Cycle II -->
