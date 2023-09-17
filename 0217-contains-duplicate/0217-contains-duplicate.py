class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        d = {}
        for num in nums:
            if d.get(num):
                return True
            d[num] = d.get(num, 0) + 1
        
        return False
        