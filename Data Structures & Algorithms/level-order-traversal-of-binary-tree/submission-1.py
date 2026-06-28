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
        self.checkLevel(root, 0, res)
        return res

    res = []
    def checkLevel(self, root, depth, res):
        if not root: return []
        
        if len(res) <= depth:
            res.append([])
        
        # add current node to the correct level
        res[depth].append(root.val)

        self.checkLevel(root.left, depth + 1, res)
        self.checkLevel(root.right, depth + 1, res)
        



        

        

