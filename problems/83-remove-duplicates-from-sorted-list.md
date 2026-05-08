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
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #83 Remove Duplicates from Sorted List -->
