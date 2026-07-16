class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, remain):
            if remain == target: 
                res.append(cur.copy()) # We are making the copy of cur, so we do not modify it on next use ->
                return
            if i >= len(nums) or remain > target:
                return
            # -< 
            # 1
            cur.append(nums[i])
            backtrack(i, cur, remain + nums[i]) # 2
            # 2
            cur.pop()
            backtrack(i+1, cur, remain)
        # 3
        backtrack(0, [], 0)
        return res


            
            # USE RECC ( :| )
            # remain = target
            # while nums[i] <= target and remain > 0:
            #     cur.append(nums[i]) # 2
            #     remain = target - nums[i] # 9 - 2 = 7
                
            #     if remain in s: 
            #         cur.append(remain)
            #         remain = remain - remain
            #         i += 1
                    

            
