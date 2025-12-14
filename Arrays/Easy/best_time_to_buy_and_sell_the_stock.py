"""
Docstring for Arrays.Easy.best_time_to_buy_and_sell_the_stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #your code goes here
        # approach 1 i tried
        # max_profit = 0
        # total_number_of_days = len(prices)
        # for i in range(0, total_number_of_days):
        #     ith_day_price = prices[i]
        #     for j in range(i, total_number_of_days): 
        #         if prices[j] > ith_day_price and (prices[j] - ith_day_price > max_profit):
        #             max_profit = prices[j] - ith_day_price
        ## declaring it as 0 as, even if there is no profit we will need to return 0
        max_profit = 0
        ## tracking the least variable
        least_val = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < least_val:
                least_val = prices[i]
            # checking whether the current value's subtraction from the least value is greater than the profit
            if prices[i] - least_val > max_profit:
                max_profit = prices[i] - least_val
                    
        return max_profit


if __name__ == '__main__':
    solution = Solution()
    input_list = list(map(int, input("Enter the list of stock prices separated by space: ").strip().split(" ")))
    print(solution.maxProfit(input_list))
    