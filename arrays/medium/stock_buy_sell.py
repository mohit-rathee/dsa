def stock_buy_sell(prices):
    print(prices)
    max_profit = 0
    min_so_far = 0

    for idx, cur_val in enumerate(prices):
        if cur_val < prices[min_so_far]:
            min_so_far = idx
        profit = cur_val - prices[min_so_far]
        if max_profit < profit:
            max_profit = profit

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(stock_buy_sell(prices))
