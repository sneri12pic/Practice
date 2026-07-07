class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        res = []
        i = 0
        while i < len(operations):
            cur = operations[i]
            #res.append(cur)

            print("n: ", cur, "i: ", i)
            if cur == "D":
                #res.pop() # pop the "D"
                print(res)
                cur = res[-1] # last num in res
                doubledCur = int(cur) * 2
                res.append(str(doubledCur)) 
                print("D: ", res)
            elif cur == "C":
                res.pop()
                print("C: ", res)
            elif cur == "+": 
                s2 = res.pop() # save the num and pop again since we need to add sum of 2
                s1 = res[-1] # shifted to -1 index

                newScore = int(s1) + int(s2)
                res.append(s2)
                res.append(str(newScore)) # add a new score that "+" have created
                print("+ : ", res)
            else:
                res.append(cur)
                print(res)
            i += 1

        answer = 0
        for num in res: answer += int(num)    
        return answer
        #print(res)
