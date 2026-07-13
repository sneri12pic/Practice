class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

        # l = 0
        # r = 1
        # while r < len(prices):
        #     if prices[l] > prices[r]:
        #         minNum = prices[r]
        #         r += 1
        #     else:
        #         minNum = prices[l]
        #         maxNum = prices[r]

        #         r += 1
        #         if prices[r] > maxNum:
                    
        #             while prices[r] > maxNum and r < len(prices) -1:
        #                 maxNum = prices[r]
        #                 profit += maxNum - minNum
        #                 r += 1
        #                 print(r)
        #             # Since we have left on the next smallest += 1 at the next iteration
        #             l = r
        #             minNum = prices[l] # new min NUM
        #             r += 1 
        #         else:
        #             profit += maxNum - minNum
            
        #     l+=1
        # print(r , l)
        # print(profit)
        # return profit