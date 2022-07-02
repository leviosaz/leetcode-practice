# Problem: Given an array prices, where prices[i] is the price of a stock on the ith day. 
# Find the maximum profit by choosing a single day to buy the stock and a different day in the future to sell it. 

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum_profit = 0
        min_item = prices[0]

        for x in prices:
            if x < min_item:
                min_item = x
                continue
            tmpMax = x - min_item
            if tmpMax > maximum_profit:
                maximum_profit = tmpMax

        return maximum_profit

# Time Complexity: O(n)
# Space Complexity: O(1)
