from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        minLen = len(strs[0])
        for i in range(0, len(strs)):
            curLen = len(strs[i])
            if (curLen < minLen):
                minLen = curLen
        for j in range(minLen):
            for k in strs:
                if k[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
            

strs_in = ["flower","flow","flight","a"]
s = Solution()
ret = s.longestCommonPrefix(strs_in)