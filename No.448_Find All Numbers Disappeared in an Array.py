class Solution:
    def findDisappearedNumbers(self, nums):

        i = 1
        appeardSet = set(nums)
        output = []
        
        while i <= len(nums):
            if i not in appeardSet:
                output.append(i)
                i += 1
            else:
                i += 1
        return output


s = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(s.findDisappearedNumbers(nums))