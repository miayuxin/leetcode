class Solution:
    def lengthOfLastWord(self, s):
        
        if len(s) == 0:
            return 0
        
        i = len(s) - 1
        count = 0
        
        # If the s is ["Hello   "], remove the trailing space, 
        # till the char shows.
        
        while (i >= 0 and s[i] == ' '):
            i -= 1

        while (i >= 0 and s[i] != ' '):
            count += 1
            i -= 1
            
        return count

s = Solution()
str = 'Hello World'
print(s.lengthOfLastWord(str))