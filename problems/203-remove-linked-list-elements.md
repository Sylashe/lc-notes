# 203. Remove Linked List Elements

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Linked List` `Recursion`

## Problem

> Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.    Example 1:   Input: head = [1,2,6,3,4,5,6], val = 6 Output: [1,2,3,4,5]   Example 2:   Input: head = [], val = 1 Output: []   Example 3:   Input: head = [7,7,7,7], val = 7 Output: []     Constraints:   	The number of nodes in the list is in the range [0,...

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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head.next != None:
            post = head.next
            if head.val == val:
                prev.next = post
            else:
                prev = head
            head = head.next
        if head.val == val:
            prev.next = None
        return dummy.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #203 Remove Linked List Elements -->
