# Find the fibonacci nth value using dynamic programming
# Memoization Approach(Top Down Approach)


def rec(n, dp):
    # Base case
    if n == 0 or n == 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    dp[n] = rec(n-1, dp) + rec(n-2, dp )
    
    return dp[n]

def fibonacci(n):
    dp = [-1] * (n+1)
    
    return rec(n , dp)
    
print(fibonacci(6))