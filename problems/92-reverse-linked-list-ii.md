# 92. Reverse Linked List II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Linked List`

## Problem

> Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.    Example 1:   Input: head = [1,2,3,4,5], left = 2, right = 4 Output: [1,4,3,2,5]   Example 2:   Input: head = [5], left = 1, right = 1 Output: [5]     Constraints:   	The number of nodes in the list is n. 	1...

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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        p0 = dummy
        for _ in range(left - 1):
            p0 = p0.next
        prev = None
        cur = p0.next
        start = cur
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        p0.next = prev
        start.next = cur
        return dummy.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #92 Reverse Linked List II -->
