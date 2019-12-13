def heapify(nums, n, i):
    l = 2*i+1
    r = 2*i+2
    largest = i
    if l<n and nums[l] > nums[largest]:
        largest = l
    if r<n and nums[r] > nums[largest]:
        largest = r

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)

def heap_sort(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):
        heapify(nums, n, i)

    for i in range(n-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0] 
        heapify(nums, i, 0)
        
    return nums

def heap_select(nums,k): #the Kth largest
    n = len(nums)
    for i in range(n-1, -1, -1):
        heapify(nums, n, i)

    for i in range(n-1, n-1-k, -1):
        nums[0], nums[i] = nums[i], nums[0] 
        heapify(nums, i, 0)
    
    return nums[n-k]
