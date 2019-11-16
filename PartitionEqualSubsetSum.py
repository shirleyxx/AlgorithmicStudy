#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 > 0 or len(nums) < 2:
            return False
        
        n = len(nums)
        m = sum(nums)//2
        f = [[False]*(m+1) for i in range(n+1)]
        
        for i in range(1, n+1):
            f[i][0] = True
            for j in range(1, m+1):
                f[i][j] = f[i-1][j] or f[i-1][j-nums[i-1]]
        
        return f[n][m]
        
        

