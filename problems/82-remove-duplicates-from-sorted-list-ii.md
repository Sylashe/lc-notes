# 82. Remove Duplicates from Sorted List II

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Linked List` `Two Pointers`

## Problem

> Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.    Example 1:   Input: head = [1,2,3,3,4,4,5] Output: [1,2,5]   Example 2:   Input: head = [1,1,1,2,3] Output: [2,3]     Constraints:   	The number of nodes in the list is in the range [0, 300]. 	-100 <= Node.val <= 100...

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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy = ListNode(None)
        dummy.next = head
        cur = head
        pre = dummy
        nxt = cur.next
        while nxt:
            if nxt.val != cur.val:
                cur.next = nxt
                pre = cur
                cur = nxt
                nxt = nxt.next
            else:
                while nxt.next and nxt.val == nxt.next.val:
                    nxt = nxt.next
                nxt = nxt.next
                cur = pre
                cur.next = nxt
                cur = nxt
                if nxt:
                    nxt = nxt.next
        return dummy.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #82 Remove Duplicates from Sorted List II -->
