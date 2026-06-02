class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = []
        j = 0
        for i in range(len(digits)):
            arr.append(digits[i])
            j = i
        if arr[j] == 9:
            while j != -1:
                if arr[j] == 9 and j != 0:
                    arr[j] = 0
                elif arr[j] != 9 and j != 0:
                    arr[j] = arr[j] + 1
                    return arr
                elif arr[j] != 9 and j == 0:
                    arr[j] = arr[j] + 1
                else:
                    arr[j] = 1
                    arr.append(0)
                j -= 1
        else:
            arr[j] = arr[j]+1
            return arr
        return arr



        
        