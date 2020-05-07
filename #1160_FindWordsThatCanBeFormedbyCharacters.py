class Solution:

    def wordCanBeFormed(self, word:str, chars:str):
        chars_list = list(chars)
        for char in word:
            if char in chars_list:
                chars_list.remove(char)
            else:
                return False
        return True

    def countCharacters(self, words: [str], chars: str) -> int:
        
        sum = 0

        for word in words:
            if self.wordCanBeFormed(word, chars) == True:
                sum += len(word)
                
        return sum 
            

words = ["cat", "bt", "hat", "tree"]
chars = "atach"

s = Solution()
print(s.wordCanBeFormed(words, chars))
print(s.countCharacters(words, chars))