from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check_dic = {}
        for i in range(len(nums)):
            if nums[i] in check_dic:
                check_dic[nums[i]] += 1
            else:
                check_dic[nums[i]] = 1

        check_dic = sorted(check_dic.items(), key = lambda x: x[1], reverse = True) 
        
        ans = []
        for i in range(k):
            ans.append(check_dic[i][0])
        return ans 


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
