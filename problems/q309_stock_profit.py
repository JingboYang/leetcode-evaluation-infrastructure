def maxProfit(prices):

    buy = [None] * (1 + len(prices))
    sell = [None] * (1 + len(prices))

    buy[0] = -prices[0]
    buy[1] = max(-prices[0], -prices[1])
    sell[0] = 0


    for i, p in enumerate(prices):
        
        if i == 0:
            continue

        sell[i] = max(sell[i - 1], buy[i - 1] + p)

        if i == 1:
            continue
        buy[i] = max(buy[i - 1], sell[i - 2] - p)

    print(prices)
    print(sell)
    print(buy)
    print('--')


maxProfit([1,2,3,0,2])