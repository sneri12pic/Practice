class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        res = []
        i = 0
        while i < len(operations):
            cur = operations[i]

            if cur == "D":
                doubledCur = int(res[-1]) * 2
                res.append(str(doubledCur)) 

            elif cur == "C":
                res.pop()
            elif cur == "+": 
                s2 = res.pop() # save the num and pop again since we need to add sum of 2
                s1 = res[-1] # shifted to -1 index

                newScore = int(s1) + int(s2)
                res.append(s2)
                res.append(str(newScore)) # add a new score that "+" have created
            else:
                res.append(cur)
            i += 1

        answer = 0
        for num in res: answer += int(num)    
        return answer
