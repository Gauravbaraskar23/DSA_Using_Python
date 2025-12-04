# 121. Best time to buy and sell stock on ith day ||

prices = [7,1,5,3,6,4]

profit = 0
n = len(prices)

for i in range(n-1):
    if prices[i+1] > prices[i]:
        profit += (prices[i+1] - prices[i]) 
    
print(profit)

