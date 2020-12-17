class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n = n-1
            else:
                nums1[m+n-1] = nums1[m-1]
                m = m-1
        
        if m == 0:
            nums1[:n] = nums2[:n]
        return nums1
        
        

s = Solution()
nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]
m = 3
n = 3
print(s.merge(nums1, m, nums2, n))