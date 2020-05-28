from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        lookup = {"(": ")", "[": "]", "{":"}"}
        for parentheses in s:
            if parentheses in lookup:
                stack.append(parentheses)
            elif len(stack) == 0 or lookup[stack.pop()] != parentheses:
                return False 
            
        if len(stack) == 0:
            return True
        else: 
            return False
s = Solution()
print(s.isValid("([)]"))


