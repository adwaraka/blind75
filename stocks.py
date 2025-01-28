# Best time to buy and sell stock; easy
def buySellStocks(stocks: list):
    maxProfit = float('-inf')
    left, right = 0, 1  #  left is buy, right is sell
    for _ in range(len(stocks) - 1):
        if stocks[left] < stocks[right]:
            profit = stocks[right] - stocks[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right
        right+=1
    return maxProfit

stocks = [7, 1, 9, 3, 6, 4]
print(buySellStocks(stocks))
