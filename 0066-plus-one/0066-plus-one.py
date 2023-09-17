class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        origin_digit = 0
        len_digits = len(digits)
        idx = 0 
        while idx < len_digits:
            
            origin_digit += pow(10, len_digits-idx-1) * digits[idx]
            idx += 1
        
        one_larger_digit = origin_digit + 1
        
        return [int(num) for num in str(one_larger_digit)]
            
        