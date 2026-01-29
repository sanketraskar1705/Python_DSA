# Problem :- Best Time to Buy and Sell Stock
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

# Optimal Soltuion
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        max_profit = 0
        min_price = float('inf')
        for i in range(n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit

s1= Solution()
print(s1.maxProfit([7,1,5,3,6,4]))

"""
Logic:
- We want to buy the stock at the lowest price and sell it later at the highest price.
- Traverse the array once.

Steps:
1. Keep track of the minimum price seen so far (min_price).
2. For each day:
   - Update min_price if today's price is lower.
   - Calculate profit if sold today: prices[i] - min_price.
   - Update max_profit if this profit is greater.
3. Return max_profit at the end.
4. If no profit is possible, max_profit remains 0.

Time Complexity: O(n)
Space Complexity: O(1)
"""
