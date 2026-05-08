# 206. Reverse Linked List

**Link:** https://leetcode.com/problems//
**Difficulty:** Easy
**Tags:** `Linked List` `Recursion`

## Problem

> Given the head of a singly linked list, reverse the list, and return the reversed list.    Example 1:   Input: head = [1,2,3,4,5] Output: [5,4,3,2,1]   Example 2:   Input: head = [1,2] Output: [2,1]   Example 3:   Input: head = [] Output: []     Constraints:   	The number of nodes in the list is the range [0, 5000]. 	-5000 <= Node.val <= 5000     Follow up: A linked list can be reversed either ite...

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(pre, cur):
            if cur == None:
                return pre
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            return helper(pre, cur)
        return helper(None, head)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #206 Reverse Linked List -->
