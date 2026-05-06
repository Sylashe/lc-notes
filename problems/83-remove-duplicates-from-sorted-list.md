# 83. Remove Duplicates from Sorted List

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Linked List`

## Problem

> Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.    Example 1:   Input: head = [1,1,2] Output: [1,2]   Example 2:   Input: head = [1,1,2,3,3] Output: [1,2,3]     Constraints:   	The number of nodes in the list is in the range [0, 300]. 	-100 <= Node.val <= 100 	The list is guaranteed to be sorted in ascen...

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
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        nxt = head
        while nxt:
            if nxt.val != cur.val:
                cur.next = nxt
                cur = nxt
            else:
                cur.next = nxt.next
            nxt = nxt.next
        return dummy.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #83 Remove Duplicates from Sorted List -->
