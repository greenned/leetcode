class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        idx = 0
        while idx < k:
            nums.insert(0, nums.pop(-1))
            idx += 1
        
        
        
        # Fail time limit
        # for _ in range(k):
        #     len_nums = len(nums)
        #     idx = len_nums - 1
        #     while idx > 0:
        #         nums[idx-1], nums[idx] = nums[idx], nums[idx-1]
                # idx -= 1
            
        