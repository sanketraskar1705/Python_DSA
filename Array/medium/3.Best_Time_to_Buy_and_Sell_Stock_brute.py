# Problem :- Best Time to Buy and Sell Stock
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

# Brute Soltuion

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        max_val = 0
        for i in range(n):
            for j in range(i+1,n):
                if prices[i] < prices[j]:
                    p = prices[j] - prices[i]
                    max_val = max(max_val,p)

        return max_val

s1 = Solution()
prices = [4,2,4,6,9,2,5]
print(s1.maxProfit(prices))

"""
Logic (Brute Force):

- Try every possible pair of days.
- Buy on day i and sell on a future day j (j > i).
- If selling price is greater than buying price:
    profit = prices[j] - prices[i]
- Keep track of the maximum profit found.
- If no profitable transaction exists, return 0.

Time Complexity: O(n^2)  -> two nested loops
Space Complexity: O(1)
"""

