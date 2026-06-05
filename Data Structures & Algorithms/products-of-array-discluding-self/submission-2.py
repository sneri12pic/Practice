class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for r in range(len(nums)):
            seen = nums.copy()
            # remove by index, not by value
            seen.pop(r)
            product = 1
            for num in seen:
                product *= num
            output.append(product)
        return output
