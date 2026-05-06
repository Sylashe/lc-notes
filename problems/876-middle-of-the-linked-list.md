# 876. Middle of the Linked List

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Linked List` `Two Pointers`

## Problem

> Given the head of a singly linked list, return the middle node of the linked list.  If there are two middle nodes, return the second middle node.    Example 1:   Input: head = [1,2,3,4,5] Output: [3,4,5] Explanation: The middle node of the list is node 3.   Example 2:   Input: head = [1,2,3,4,5,6] Output: [4,5,6] Explanation: Since the list has two middle nodes with values 3 and 4, we return the s...

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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #876 Middle of the Linked List -->
