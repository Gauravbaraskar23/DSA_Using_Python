# 1672. Richest Customer Wealth

# accounts = [[1,2,3] , [3,2,1]]
accounts = [[1,2,3] , [3,2,1], [6,5]]


ans = 0
for account in accounts:
    ans = max(ans, sum(account))
    
print(ans)