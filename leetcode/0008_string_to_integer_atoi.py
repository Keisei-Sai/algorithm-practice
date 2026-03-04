class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n and s[i] == " ":
            i += 1
        if i == n:
            return 0
        
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        
        res = 0
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        
        result = sign * res

        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX

        return result
