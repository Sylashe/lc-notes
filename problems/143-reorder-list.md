# 143. Reorder List

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Linked List` `Two Pointers` `Stack` `Recursion`

## Problem

> You are given the head of a singly linked-list. The list can be represented as:   L0 &rarr; L1 &rarr; &hellip; &rarr; Ln - 1 &rarr; Ln   Reorder the list to be on the following form:   L0 &rarr; Ln &rarr; L1 &rarr; Ln - 1 &rarr; L2 &rarr; Ln - 2 &rarr; &hellip;   You may not modify the values in the list's nodes. Only nodes themselves may be changed.    Example 1:   Input: head = [1,2,3,4] Output:...

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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse_list(head):
            cur = head
            prev = None
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        def middle_node(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        mid = middle_node(head)
        second = mid.next
        second = reverse_list(second)
        first = head
        mid.next = None
        dummy = ListNode(0)
        dummy.next = head
        while second:
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1
            first = next1
            second = next2
        return dummy.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #143 Reorder List -->
