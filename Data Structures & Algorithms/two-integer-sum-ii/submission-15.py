class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) -1

        while l < r:
            currSum  = numbers[l] + numbers[r]

            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return[l+1, r+1]

        # if min(numbers) < 0 and target == max(numbers):
        #     print("Error")
        # if target > 0:
        #     idx1 = 1
        #     n = numbers[0] # Smallest
        #     val_idx2 = target - n

        #     # Find index of val_idx2
        #     counter = 1
        #     for num in numbers:

        #         if num == val_idx2:
        #             return [idx1, counter]
        #         counter += 1    

        #     #print('t:', target)
        #     #print('idx1:', idx1)
        #     #print('idx2:', idx2)
        # else:
        #     idx1 = 1
        #     smallest = numbers[0] # Smallest
        #     val_idx2 = target - smallest



        
