# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = []
        self.checkDepth(root, 0, res)
        
        return res
        
        
    def checkDepth(self, root, depth, res):
            if not root:
                return

            # create the level if it does not exist yet
            if len(res) <= depth:
                res.append([])

            # add current node to the correct level
            res[depth].append(root.val)

            # go left and right, depth increases
            self.checkDepth(root.left, depth + 1, res)
            self.checkDepth(root.right, depth + 1, res)


        

        

