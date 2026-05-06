# 61. Rotate List

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Linked List` `Two Pointers`

## Problem

> Given the head of a linked list, rotate the list to the right by k places.    Example 1:   Input: head = [1,2,3,4,5], k = 2 Output: [4,5,1,2,3]   Example 2:   Input: head = [0,1,2], k = 4 Output: [2,0,1]     Constraints:   	The number of nodes in the list is in the range [0, 500]. 	-100 <= Node.val <= 100 	0 <= k <= 2 * 109

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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        end = None
        new_start = None
        if not head or head.next == None:
            return head
        while cur:
            end = cur
            cur = cur.next
            n += 1
        if k % n == 0 or n == 0:
            return head
        k %= n
        new_end = head
        for _ in range(n - k - 1):
            new_end = new_end.next
        new_start = new_end.next
        new_end.next = None
        end.next = head
        return new_start
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #61 Rotate List -->
