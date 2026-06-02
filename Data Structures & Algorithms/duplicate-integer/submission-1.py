class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums) - 1):
            num1 = nums[i] # take firs number
            num2 = nums[i+1] # take neighbour 

            # If neighbour equal: dupe, no: next neighbours
            if num1 == num2:
                return True   
            elif i == len(nums) - 1: 
                return False
        return False