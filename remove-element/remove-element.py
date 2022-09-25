class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        pointer = 0
        while val in nums:
            if nums[pointer] == val:
                nums.pop(pointer)
                pointer = 0
            else:
                pointer += 1
            
        return len(nums)
        