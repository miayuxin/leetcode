class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        
        while (left < right):
            twoSum = numbers[left] + numbers[right]
            
            # Example shows index 0 return 1, so the index need + 1 
            if twoSum == target:
                return left + 1, right + 1 
            elif twoSum > target:
                right -= 1
            else:
                left += 1
