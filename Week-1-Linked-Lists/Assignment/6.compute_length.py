# Complete the getLength function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getLength(A):
    count = 0
    while A:
        count += 1
        A = A.next
    return count
