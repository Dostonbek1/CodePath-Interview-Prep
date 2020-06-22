# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        cur_level = [root]
        while True:
            if not any(cur_level):
                return True
            # check if symmetric
            if not self._isSymmetric(cur_level):
                return False
            
            next_level = list()
            for n in cur_level:
                if n:
                    next_level.append(n.left)
                    next_level.append(n.right)
                
            cur_level = next_level
        
        return True
            
    def _isSymmetric(self, lst):
        head, tail = 0, len(lst)-1
        while head < tail:
            h, t = lst[head], lst[tail]
            if h == t == None:
                continue 
            if None in (h, t) or h.val != t.val:
                return False
            head += 1
            tail -= 1
        return True
        