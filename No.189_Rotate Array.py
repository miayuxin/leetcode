class Solution:
    
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.

        """

        N = len(nums)
        k %= N
        self.reverse(nums, 0, N - 1 - k)
        self.reverse(nums, N - k, N - 1)
        self.reverse(nums, 0, N - 1)

    def reverse(self, nums, start, end):
        while (start <= end):
            tempStart = nums[start]
            tempEnd = nums[end]
            nums[start] = tempEnd
            nums[end] = tempStart
            start += 1
            end -= 1

s = Solution()
nums = [-1, -100, 3, 99]
k = 2
print(s.rotate(nums, k))

