class Solution:
    def reverse(self, x: int) -> int:
        #if x >= 0, reverse str(x)
        if x >= 0:
            out = int(str(x)[::-1])
        #if x < 0, eliminate "-" from x and reverse it, then add "-"
        else:
            out = int("-" + str(-x)[::-1])

        #output have to be 32-bit signed integer.
        if out <= -2**31 or out >= 2**31 - 1:
            return 0
        else:
            return out
