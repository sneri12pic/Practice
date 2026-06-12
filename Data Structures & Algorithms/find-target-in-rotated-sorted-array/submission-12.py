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
                    print("Left M:", nums[mid])
                    r = mid - 1   
                else:
                    print("Right M:",nums[mid])
                    l = mid + 1
            else:
                if target == nums[mid]:
                    return mid 
                if target >= nums[mid] and target <= nums[r]:
                    print("Right M:",nums[mid])
                    l = mid + 1
                else:
                    print("Left M:", nums[mid])
                    r = mid - 1   
        return -1