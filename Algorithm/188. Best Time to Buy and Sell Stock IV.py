class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        # k is big enough to cover all ramps
        if k >= len(prices) // 2:
            return sum(x - y
                        for x, y in zip(prices[1:], prices[:-1])
                        if x > y)

        profits = [0] * len(prices)
        # compare profit we have made and new profit we got in jth transactions
        # profit_sum: profit we have made + new profit
        for _ in range(k):
            profit_sum = 0
            for i in range(1, len(prices)):
                profit = prices[i] - prices[i-1]
                profit_sum = max(profit_sum+profit, profits[i])
                profits[i] = max(profit_sum, profits[i-1])
        
        return profits[-1]