class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        sorts = sorted(list(set(nums)))
        if len(sorts) < 3:
            return sorts[-1]
        else:
        
            return sorts[-3]