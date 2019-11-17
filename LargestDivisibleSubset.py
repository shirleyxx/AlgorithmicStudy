class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        size = [1]*n
        element = []
        
        if n < 2:
            return nums
        
        nums = sorted(nums)
        for i in range(n):
            sub = []
            for j in range(i):
                if nums[i]%nums[j] == 0 and size[i]<=size[j]+1:
                    size[i] = size[j]+1
                    sub = element[j].copy() # must use 'copy'
            sub.append(nums[i])
            element.append(sub)
        idx = size.index(max(size))
        return element[idx]