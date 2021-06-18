 
# Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change? If it’s not possible to make change, print -1.

import sys

def coinchange(V, coins):
    dp = [0] * (V+1) 

    dp[0] = 0
    for i in range(1, V+1):
        dp[i] = sys.maxsize

    for i in range(1, V+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                sub_res = dp[i-coins[j]]
                if sub_res != sys.maxsize and sub_res + 1 < dp[i]:
                    dp[i] = sub_res + 1
    
    if dp[i] == sys.maxsize:
        return -1 

    return dp[-1]