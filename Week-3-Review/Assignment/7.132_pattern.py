# https://leetcode.com/problems/132-pattern/

def find132pattern(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    Ai = float('-inf')
    stack = []

    for i in range(len(nums)-1, -1, -1):
        if nums[i] < Ai:
            return True
        while stack and nums[i] > stack[-1]:
            Ai = stack.pop()
        stack.append(nums[i])

    return False