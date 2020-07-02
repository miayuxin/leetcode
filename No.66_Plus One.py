class Solution:
    def plusOne(self, digits):
        
        num = ''.join(map(str, digits))
        num = int(num) + 1

        newList = []
        for i in str(num):
            i = int(i)
            newList.append(i)
        return newList

s = Solution()
l1 = [1, 2, 3]
print(s.plusOne(l1))