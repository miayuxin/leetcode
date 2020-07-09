class Solution:
    def fib(self, N):
        
        if N == 0 or N == 1:
            return N
        
        res = self.fib(N - 2) + self.fib(N - 1)
        return res

s = Solution()
input = 2
print(s.fib(input))