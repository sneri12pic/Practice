
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 1:
            return []

        res = []
        cur = []
        def backtrack(index):
            if index >= len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[index])
            backtrack(index+1)
            cur.pop()
            backtrack(index+1)

        backtrack(0)
        return res