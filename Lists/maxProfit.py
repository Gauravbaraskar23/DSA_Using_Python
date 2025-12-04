# 121. Best time to buy and sell stock on ith day 
prices  = [7,1,5,3,6,4]

min_price = prices[0]
profit = 0

for i in range(1, len(prices)):
    curr_profit = prices[i] - min_price
    if curr_profit > profit:
        profit = curr_profit
    min_price = min(min_price, prices[i])
         
print(profit)
