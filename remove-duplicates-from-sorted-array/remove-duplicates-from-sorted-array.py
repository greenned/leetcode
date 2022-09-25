class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        
        while pointer < len(nums):
            target = nums[pointer]
            idx = pointer + 1    
            while target in nums[pointer+1:]:
                if nums[idx] == target:
                    nums.pop(idx)
                else:
                    idx += 1
            pointer += 1
        return len(nums)