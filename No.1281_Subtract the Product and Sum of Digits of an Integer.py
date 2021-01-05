class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        strn = str(n)
        pronum = 1
        addnum = 0
        for i in strn:
            pronum *= int(i)
            addnum += int(i)
        return pronum - addnum
