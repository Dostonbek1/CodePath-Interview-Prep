'''
Write a program to find the node at which the intersection of two singly linked lists begins.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the 
two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, 
it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 
3 nodes before the intersected node in B. 

Notes:
    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        a_pointer = headA
        b_pointer = headB
        
        while (a_pointer != b_pointer):
            if a_pointer:
                a_pointer = a_pointer.next
            else:
                a_pointer = headB
                
            if b_pointer:
                b_pointer = b_pointer.next
            else:
                b_pointer = headA
                
        return a_pointer
        