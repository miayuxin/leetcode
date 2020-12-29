class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                res += "G"
                i = i + 1
            elif command[i] == "(" and command[i+1] == ")":
                res += "o"
                i = i + 2
            elif command[i] == "(" and command[i+3] == ")":
                res += "al"
                i = i + 4
        return res