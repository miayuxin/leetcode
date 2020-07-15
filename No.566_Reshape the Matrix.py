class Solution:
    def matrixReshape(self, nums, r, c):
        
        M, N = len(nums), len(nums[0])
        
        if M * N != r * c:
            return nums
        
        res = []
        row = []
        
        for i in range(M):
            for j in range(N):
                row.append(nums[i][j])
                if len(row) == c:
                    res.append(row)
                    row = []
        return res

s = Solution()
nums = [[1,2,3,4]]
r = 2
c = 2
print(s.matrixReshape(nums, r, c))
            