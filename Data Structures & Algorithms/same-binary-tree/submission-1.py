# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Condition: if p.right != q.right False
        if not q and not p:
            return True
        if p and not q or not p and q:
            return False
        # How do we get to the root node of each? And do we need that?
        
        # Logic : Return True if p.right = q.right | p,q left
        if p.val == q.val:
            # Continue recurssion until the end of left
            resL = self.isSameTree(p.left, q.left) # make rec on the left
            resR = self.isSameTree(p.right, q.right)
            print("L",resL," R: ", resR)
            # if both are same
            if resL != False and resR != False:
                return True
        else:
            return False
        return False
