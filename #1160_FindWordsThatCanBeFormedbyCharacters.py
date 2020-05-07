class Solution:
    def countCharacters(self, words: [str], chars: str) -> int:
        
        sum = 0
        
        for word in words:
            chars_list = list(chars)
            for char in word:
                if char in chars_list:
                    chars_list.remove(char)
                else:
                    break
            else:
                sum += len(word)
        return sum
                

words = ["cat", "bt", "hat", "tree"]
chars = "atach"

s = Solution()
print(s.countCharacters(words, chars))