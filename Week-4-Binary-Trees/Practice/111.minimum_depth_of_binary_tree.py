'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        depth = 1
        cur_level = [root]
        
        while cur_level:
            nxt_level = list()
            for node in cur_level:
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)
                if node.right == node.left == None:
                    return depth
            depth += 1    
            cur_level = nxt_level
    