# 148. Sort List

**Link:** https://leetcode.com/problems//
**Difficulty:** Medium
**Tags:** `Linked List` `Two Pointers` `Divide and Conquer` `Sorting` `Merge Sort`

## Problem

> Given the head of a linked list, return the list after sorting it in ascending order.    Example 1:   Input: head = [4,2,1,3] Output: [1,2,3,4]   Example 2:   Input: head = [-1,5,3,4,0] Output: [-1,0,3,4,5]   Example 3:   Input: head = [] Output: []     Constraints:   	The number of nodes in the list is in the range [0, 5 * 104]. 	-105 <= Node.val <= 105     Follow up: Can you sort the linked list...

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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mid_list(head):
            slow = fast = head
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            pre.next = None
            return slow
        def merge_list(head1, head2):
            dummy = ListNode(0)
            cur = dummy
            while head1 and head2:
                if head1.val <= head2.val:
                    cur.next = head1
                    head1 = head1.next
                else:
                    cur.next = head2
                    head2 = head2.next
                cur = cur.next
            if head1:
                cur.next = head1
            else:
                cur.next = head2
            return dummy.next
        if head == None or head.next == None:
            return head
        head1 = head
        head2 = mid_list(head)
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return merge_list(head1, head2)
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #148 Sort List -->
