class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        sorts = sorted(nums)
        
        # if the max num is positive, means the negative may exist,
        # compare: if all nums are positive & if both negative and positive exist. 
        # if the max num is negative, means all nums are negative, consider 2
        # negatives make a positive.

        if sorts[-1] < 0:
            return sorts[-1] * sorts[-2] * sorts[0]
        else:
            a = sorts[-1] * sorts[-2] * sorts[-3]
            b = sorts[-1] * sorts[0] * sorts[1]
            return max(a, b)

