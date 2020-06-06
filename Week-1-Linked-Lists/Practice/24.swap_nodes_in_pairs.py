'''
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
    Given 1->2->3->4, you should return the list as 2->1->4->3.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur.next and cur.next.next:
            # set two pointers to new pair
            first = cur.next
            sec = cur.next.next
            # swap nodes in pair
            cur.next = sec
            first.next = sec.next
            sec.next = first
            # update cur pointer by moving by two nodes
            cur = cur.next.next

        return dummy.next  