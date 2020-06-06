'''
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        st = set()
        lst = []
        while head:
            if head.val not in st:
                lst.append(head.val)
            elif head.val in st and head.val in lst:
                lst.remove(head.val)
            st.add(head.val)
            head = head.next
            
        ans = cur = ListNode(0)
        for num in lst:
            cur.next = ListNode(num)
            cur = cur.next
        return ans.next

    def deleteDuplicates2(self, head):
        dummy = ListNode(0)  # construct a dummy node
        dummy.next = head 
        pre = dummy           # set up pre and cur pointers
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                # loop until cur point to the last duplicates
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next  # propose the next for pre
                                     # this will be verified by next line
            else:
                pre = pre.next 
            cur = cur.next
        return dummy.next