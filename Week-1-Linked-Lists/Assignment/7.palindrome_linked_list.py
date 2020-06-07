# Complete the isPalindrome function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def isPalindrome(A):
    slow = A
    fast = A

    def reverse(head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    
    slow = reverse(slow)
    fast = A
    
    while slow:
        if (slow.data != fast.data):
            return False
        slow = slow.next
        fast = fast.next
    
    return True