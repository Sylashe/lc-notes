# 237. Delete Node in a Linked List

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Linked List`

## Problem

> There is a singly-linked list head and we want to delete a node node in it.  You are given the node to be deleted node. You will not be given access to the first node of head.  All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.  Delete the given node. Note that by deleting the node, we do not mean removing it from me...

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
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #237 Delete Node in a Linked List -->
