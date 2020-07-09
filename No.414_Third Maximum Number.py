class Solution:
    def compare(self, num1, num2) -> bool: # return if num1 > num2. None always the smallest number
        if num1 == None:
            return False
        elif num2 == None:
            return True
        return num1 > num2

    def thirdMax(self, nums):    
        largest, secondMax, thirdMax = None, None, None

        nums = set(nums)

        for num in nums:
            if self.compare(num, largest):
                largest, secondMax, thirdMax = num, largest, secondMax
            elif self.compare(num, secondMax): 
                thirdMax = secondMax
                secondMax = num
            elif self.compare(num, thirdMax):
                thirdMax = num
        
        if thirdMax == None:
            return largest
        return thirdMax 

s = Solution()
nums = [5, 2, 2]
print(s.thirdMax(nums))