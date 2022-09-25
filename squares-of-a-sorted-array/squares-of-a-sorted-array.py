class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            nums[idx] = pow(nums[idx],2)
        
        return sorted(nums)
        