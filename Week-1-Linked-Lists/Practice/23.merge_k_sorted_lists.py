'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pre = cur = ListNode(0)
           
        heap = []
        for i in range(len(lists)):
            if lists[i]: 
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            cur.next = node[2]  
            cur = cur.next
            
            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))

        return pre.next
        