#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')]*(amount+1) for i in range(n+1)]
        
        for i in range(n+1):
             dp[i][0] = 0
        
        for i in range(1, n+1):
             for j in range(amount+1):
                if j < coins[i-1]:  
                      dp[i][j] = dp[i-1][j]
                else:
                      dp[i][j] = min(dp[i][j-coins[i-1]]+1, dp[i-1][j])
        
        if dp[n][amount] < float('inf'):
            return dp[n][amount]
        else:
            return -1
        

