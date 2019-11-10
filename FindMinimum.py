class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]   
        left = 0 
        right = len(nums)-1
        mid = (left + right)//2
        while left < right:
            if nums[mid]>nums[left]:
                left = mid
            else:
                right = mid
            mid = (left + right)//2
        return min(nums[mid], nums[mid+1], nums[0])