class Solution:
    def reverse(self, x: int) -> int: # object function / class
        # -2147483412
        # -2147483648 ~ 2147483647
        res = 0 
        
        # return the absolute input value of x
        num = abs(x)
        
        while (num != 0):
            temp = num % 10
            res = res * 10 + temp
            num = int(num/10)
            
        if x > 0 and num < 2147483647:
            return res
        elif x < 0 and num <= 2147483647:
            return -res
        else:
            return 0


s = Solution()
print(s.reverse(-2147483412))
