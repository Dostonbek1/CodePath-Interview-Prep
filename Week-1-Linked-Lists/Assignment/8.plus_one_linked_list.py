# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def addOne(A):
    stack = []
    head = A
    while head:
        stack.append(head.data)
        head = head.next
    
    count = 0
    carry = 0
    ans = SinglyLinkedListNode(0)
    while stack or carry:
        if stack:
            carry += stack.pop() 
        if count == 0:
            carry += 1
            count += 1
        carry, val = divmod(carry, 10)
        ans.data = val
        head = SinglyLinkedListNode(0)
        head.next = ans
        ans = head
    return ans.next