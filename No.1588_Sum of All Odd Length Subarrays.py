from typing import List
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for subarray_length in range(1, len(arr)+1, 2):
            temp_2 = self.subArrayCnt(arr, subarray_length)
            res += temp_2
        return res
    
    def subArrayCnt(self, arr, subLen):
        total = 0
        for i in range(len(arr) - subLen + 1):
            temp = arr[i: i + subLen]
            total += sum(temp) 
        return total

s = Solution()
print(s.subArrayCnt([1, 4, 2, 5, 3], 3))
print(s.sumOddLengthSubarrays([1, 4, 2, 5, 3]))