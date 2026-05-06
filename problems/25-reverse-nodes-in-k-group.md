# 25. Reverse Nodes in k-Group

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Linked List` `Recursion`

## Problem

> Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.  k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.  You may not alter the values in the list's nodes, only nodes themselves may be changed.    Example 1:   I...

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        prev = None
        cur = head
        prev_tail = dummy
        while n >= k:
            tail = cur
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            prev_tail.next = prev
            tail.next = cur
            prev_tail = tail
            n -= k
        return dummy.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #25 Reverse Nodes in k-Group -->
