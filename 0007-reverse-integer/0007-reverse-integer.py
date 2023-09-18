class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        new_value = 0
        str_x = str(abs(x))
        len_str_x = len(str_x)
        for power, value in enumerate(str_x):
            new_value += pow(10, power) * int(value)
        
        result = new_value * sign
        
        if result <= -pow(2,31) or result >= pow(2,31):
            return 0 
        else:
            return result
        