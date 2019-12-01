class Solution:
     def getKth(self, nums1, nums2, k, extra): #can generate to k 
         l1 = len(nums1)
         l2 = len(nums2)
         if l1>l2:
             nums1, nums2 = nums2, nums1
             l1, l2 = l2, l1
         if l1 == 0:
             if extra:
                 return (nums2[k-1]+nums2[k])/2
             else:
                 return nums2[k-1]
         if k==1:
             if extra:
                 return (min(nums1[0], nums2[0]) + self.getKth(nums1, nums2, 2, False))/2
             else:
                 return min(nums1[0], nums2[0]) 
            
         i1 = min(k//2, l1)
         i2 = k-i1
         if nums1[i1-1]<= nums2[i2-1]:
             return self.getKth(nums1[i1:], nums2, i2, extra)
         else:
             return self.getKth(nums1, nums2[i2:], i1, extra)
    
     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         len1 = len(nums1)
         len2 = len(nums2)
         if (len1 + len2) % 2 == 1: 
             return self.getKth(nums1, nums2, (len1 + len2)//2+1, False)
         else:
             return self.getKth(nums1, nums2, (len1 + len2)//2, True)
    
################### 2nd approach #####################################

    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m

        imin, imax, half_len = 0, m, (m + n + 1) //2 
        while imin <= imax:
            print(imin, imax,half_len )
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


