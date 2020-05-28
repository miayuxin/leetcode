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

# 大目標是countCharacters，if word can be formed by chars, 就返回字母數的sum.
# 小目標是wordCanBeFormed, 把word的每個字母拿出來跟chars_list對照，確認是否在chars_list裡面。
# 第一次跑時：
# chars_list = ["a", "t", "a", "c", "h"]
# word = "cat", char = "c" 
# 所以 "c" 在 chars_list 裡，就把chars_list的"c"拿掉，因為不能重複比對，剩下 chars_list = ["a", "t", "a", "h"]
# 剩下以此類推，直到"cat"結束後，會是成立的所以 return True