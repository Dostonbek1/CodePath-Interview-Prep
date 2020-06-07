'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        a = head
        a_nxt = head.next
        
        # create a stack with the nodes
        stack = []
        while head:
            stack.append(head)
            head = head.next
        b = stack.pop() # b pointer is the last node
        b_prev = None   # b_prev is the node before the last
        while a != b_prev and b != a_nxt:
            b_prev = stack.pop()
            a.next = b
            b.next = a_nxt
            b_prev.next = None
            # update a, b and a_nxt pointers 
            a = a_nxt
            b = b_prev
            a_nxt = a.next
            