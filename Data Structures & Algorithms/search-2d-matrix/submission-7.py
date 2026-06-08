class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       

        for i in range(len(matrix)):
            currM = matrix[i]
            lIdx = len(currM) - 1
            l = 0
            
            if currM[lIdx] == target:
                return True
            elif len(matrix) < 1: 
                return False
            elif len(currM) < 1:
                i += 1

            if currM[lIdx] > target:
                while l < lIdx:
                    # Check if first element is target
                    if currM[0] == target:
                        return True
                    # Starts from 1     
                    midIdx = (lIdx + l) // 2
                    if currM[midIdx] == target:
                        return True
                    if currM[midIdx] < target:
                        l = midIdx + 1
                    else:
                        lIdx = midIdx -1
        return False