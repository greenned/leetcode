class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # [0,1,0,3,12]
            
        left = 0
        for right in range(len(nums)):
            el = nums[right]
            if el != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1