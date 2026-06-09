class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        res = nums[0]
        while r >= l:
            if nums[r] > nums[l]:
                res = min(res, nums[l])
                break     
            # minimum must be to the right of mid
            mid = (r+l) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1    
        return res
