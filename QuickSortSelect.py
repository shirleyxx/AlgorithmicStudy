# Ascending
# Random pivot

import random

def partition(nums, pivot_index, left, right):
    p = nums[pivot_index]  
    nums[left], nums[pivot_index] = nums[pivot_index], nums[left] 
    # pivot at the leftest, start from the right
    while left < right:
        while nums[right] > p: #and left < right: 
            right -= 1
        nums[left] = nums[right]
        while nums[left] <= p and left < right: #at least one side '='
            left += 1
        nums[right] = nums[left]
    nums[left] = p    
    return left
        
def quick_select(nums, k, left, right):
    if left == right:
        return nums[left]

    pivot_index0 = random.choice(range(left, right+1))
    pivot_index1 = partition(nums, pivot_index0, left, right)
    
    if k-1 == pivot_index1:
        return nums[pivot_index1]
    elif k-1 < pivot_index1:
        return quick_select(nums, k, left, pivot_index1-1)
    else:
        return quick_select(nums, k, pivot_index1+1, right)
    
def quick_sort(nums, left, right):
    if left >= right:
        return 

    pivot_index0 = random.choice(range(left, right+1))
    pivot_index1 = partition(nums, pivot_index0, left, right)
    quick_sort(nums, left, pivot_index1-1)
    quick_sort(nums, pivot_index1+1, right)
    return 
    
if __name__=='__main__':
    nums1 = [0,1,2,-1,-2]
    print('Quick sort:', nums1)
    quick_sort(nums1, 0, len(nums1)-1)
    print('Sorted:    ', nums1, '\n')
    
    nums2 = [1,1,1,0]
    selected = []
    print('Quick select:', nums2)
    print('Selected:    ', [quick_select(nums2, k+1, 0, len(nums2)-1) for k in range(len(nums2))])
