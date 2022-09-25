class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman2num = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
                    }
        
        chars = list(s)
        prev = +inf
        result = 0
        for char in chars:
            if roman2num[char] // prev == 5 or roman2num[char] // prev == 10:
                result -= prev * 2
            result += roman2num[char]
            prev = roman2num[char]
        
        return result