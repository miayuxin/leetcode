class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        l = len(s)
        for i in range(0, l):
            ch = s[i]
            nextCh =  s[i + 1] if (i + 1) < l else ''
            # nextCh = ''
            # if (i + 1) < l:
            #     nextCh = s[i + 1]      
            
            if (ch == 'I'):
                if (nextCh == 'V' or nextCh == 'X'):
                    val = val - 1
                else:
                    val += 1
            elif (ch == 'V'):
                val = val + 5
            elif (ch == 'X'):
                if (nextCh == 'L' or nextCh == 'C'):
                    val -= 10
                else:
                    val = val + 10
            elif (ch == 'L'):
                val = val + 50
            elif (ch == 'C'):
                if (nextCh == 'D' or nextCh == 'M'):
                    val -= 100
                else:
                    val += 100
            elif (ch == 'D'):
                val += 500
            elif (ch == 'M'):
                val += 1000
        return val 