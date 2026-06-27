# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # # Base Case
        # if not root:
        #     return False
        # if root and not subRoot:
        #     return True
        # if not root and not subRoot:
        #     return True

        # if root and subRoot:
        #     if root.val == subRoot.val:
        #         self.isSubtree(root.left, subRoot.left) # DFS left
        #         self.isSubtree(root.right, subRoot.right) # DFS right
        #         res = True
                
        #     else:
        #         print(root.val, subRoot.val)
        #         self.isSubtree(root.left, subRoot)
        #         self.isSubtree(root.right, subRoot)
                
        # return res

        if root and not subRoot: return True
        if not root: return False
        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

        

    def sameTree(self, root, subRoot):
        if not root and not  subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            # Rec call # Left and Right are same
            return(self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        return False 



