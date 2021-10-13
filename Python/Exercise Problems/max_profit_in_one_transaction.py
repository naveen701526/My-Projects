def max_profit(stock_price):
    max_profit_amt = 0

    for i in range(len(stock_price)):
        profit_amt = 0
        for j in range(i+1, len(stock_price)):
            profit_amt = stock_price[j] - stock_price[i]
            if profit_amt > max_profit_amt:
                max_profit_amt = profit_amt
    return max_profit_amt


print(max_profit([int(x) for x in input().split()]))
