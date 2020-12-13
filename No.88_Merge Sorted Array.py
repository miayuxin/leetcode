class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # If there is no element in nums1, copy nums2 to nums1
        if m == 0:
            nums1 = nums2

        # Imagine the last position (index) in merged array
        lastPos = m + n - 1
        # Last index of nums1
        i = m - 1
        # Last index of nums2
        j = n - 1


        while i >= 0 and j >= 0 and lastPos >= 0:
            if nums1[i] <= nums2[j]:
                nums1[lastPos] = nums2[j]
                lastPos -= 1
                j -= 1
            else:
                nums1[lastPos] = nums1[i]
                nums1[i] = nums2[j]
                j -= 1
                i -= 1
                lastPos -= 1


s = Solution()
nums1 = [0]
nums2 = [1]
m = 0
n = 1
print(s.merge(nums1, m, nums2, n))