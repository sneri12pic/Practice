class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while(r >= l):
            if nums[l] == target: 
                return l
            if nums[r] == target: 
                return r  
            mid = (l+r) // 2    
            if nums[l] <= nums[mid]:
                if target == nums[mid]:
                    return mid
                if target <= nums[mid] and target >= nums[l]:
                    r = mid - 1   
                else:
                    l = mid + 1
            else: # Go Right
                if target == nums[mid]:
                    return mid 
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1   
        return -1