class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        prices: int[]
        prices[i] is the price of NeetCoin on the ith day
        
        Obj: Choose a single day to buy a neetcoin and sell in the future

        Ret: maximum profit you achieve
            - no transactions: 0
        
        '''
        # 10, 1, 5, 6, 7, 1
        # buy at 1 (prices[1]), sell at 7 (prices[4])

        # Alg:
        # 1: Find the biggest difference between two prices
            # Loop through, store a min and max
            # 7, 6, 4, 3, 1
            # 7
            # 6
            # 6 - 7 = -1, not > 0
            # 4 - 7 = -3, not > 0 
            # 3 - 7 = -4, not > 0
            # 1 - 7 = -6, not > 0
        profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]

        # O(n^2)
        return profit
                    




