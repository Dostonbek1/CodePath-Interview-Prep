r"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
    Google: 90% of our engineers use the software you wrote (Homebrew), 
    but you can’t invert a binary tree on a whiteboard so f*** off.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        self._invert(root)       
        return root
        
    def _invert(self, root):
        if not root:
            return root
        
        root.left, root.right = root.right, root.left
        self._invert(root.left)
        self._invert(root.right)

    # iterative
    def inverTree2(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
