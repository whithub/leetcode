class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_sell_price = 0
        days = len(prices)

        for day in range(days-1, -1, -1):
            todays_price = prices[day]
            profit_if_sold_today = max_sell_price - todays_price

            max_profit = max(profit_if_sold_today, max_profit)
            max_sell_price = max(max_sell_price, todays_price)

        return max_profit