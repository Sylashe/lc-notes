# 23. Merge k Sorted Lists

**Link:** https://leetcode.com/problems//
**Difficulty:** Hard
**Tags:** `Linked List` `Divide and Conquer` `Heap (Priority Queue)` `Merge Sort`

## Problem

> You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.  Merge all the linked-lists into one sorted linked-list and return it.    Example 1:   Input: lists = [[1,4,5],[1,3,4],[2,6]] Output: [1,1,2,3,4,4,5,6] Explanation: The linked-lists are: [   1->4->5,   1->3->4,   2->6 ] merging them into one sorted linked list: 1->1->2->3->4->4->5->6   Example 2:   Input...

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
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            heap = []
            for i, node in enumerate(lists):
                if node:
                    heapq.heappush(heap, (node.val, i, node))
            dummy = ListNode(0)
            cur = dummy
            while heap:
                val, i, node = heapq.heappop(heap)
                cur.next = node
                cur = cur.next
                if node.next:
                    heapq.heappush(heap, (node.next.val, i, node.next))
            return dummy.next
```

## Mistakes / Traps

<!-- What went wrong the first time -->

## Similar Problems

<!-- #23 Merge k Sorted Lists -->
