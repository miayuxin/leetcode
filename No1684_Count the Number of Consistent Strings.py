class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        appeardSet = set()
        for i in allowed:
            appeardSet.add(i)
        
        count = 0
        for i in range(0, len(words)):
            if self.checkWord(appeardSet, words[i]):
                count += 1
        return count
    
    def checkWord(self, allowedSet, word):
        for charater in word:
            if charater not in allowedSet:
                return False
        return True