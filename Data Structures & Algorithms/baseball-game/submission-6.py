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
                s1, s2 = res[-1], res[-2]
                res.append(int(s1) + int(s2)) # add a new score that "+" have created
            else:
                res.append(cur)
            i += 1

        answer = 0
        for num in res: answer += int(num)    
        return answer
