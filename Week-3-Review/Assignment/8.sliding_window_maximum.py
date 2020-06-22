
def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums:
        return
    i = 0
    j = k - 1
    ans = []

    while j < len(nums):
        ans.append(max(nums[i:j+1]))
        i += 1
        j += 1
    
    return ans