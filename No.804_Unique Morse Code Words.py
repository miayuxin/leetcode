class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # generate an [a-z] alphabet array 
        alphabet = []
        for i in range(26):
            alphabet.append(chr(ord('a') + i))
        
        morse_dict = {}
        for i in range(len(alphabet)):
                morse_dict[alphabet[i]] = morse[i]
                
        res = set()
        for word in words:
            output = ""
            for w in word:
                output += morse_dict[w]
            res.add(output)
        return len(res)