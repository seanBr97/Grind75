"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""


# works, too slow
def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, starting_price in enumerate(prices[:-1]): # can't sell last stock at a later date
            highest_future_price = max(prices[i:])
            largest_possible_profit = highest_future_price - starting_price
            if largest_possible_profit > 0 and largest_possible_profit > max_profit:
                max_profit = largest_possible_profit

        return max_profit
		
# optimised
def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        return max_profit