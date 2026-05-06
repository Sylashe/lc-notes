# 328. Odd Even Linked List

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Linked List`

## Problem

> Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.  The first node is considered odd, and the second node is even, and so on.  Note that the relative order inside both the even and odd groups should remain as it was in the input.  You must solve the problem in O(1) extra space complexity and...

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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        odd_idx = ListNode(0)
        even_idx = ListNode(0)
        even_head = even_idx
        dummy = odd_idx
        i = 1
        while head != None:
            if i == 1:
                odd_idx.next = head
                odd_idx = odd_idx.next
                i = 2
            else:
                even_idx.next = head
                even_idx = even_idx.next
                i = 1
            head = head.next
        even_idx.next = None
        odd_idx.next = even_head.next
        return dummy.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #328 Odd Even Linked List -->
