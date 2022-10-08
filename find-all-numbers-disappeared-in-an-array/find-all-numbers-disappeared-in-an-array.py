class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        
        
        # for i in range(1, len(nums)+1):
        #     if i in nums:
        #         while i in nums:
        #             nums.pop(nums.index(i))
        #     else:
        #         nums.append(i)
        # return nums
        
        set_result = set(range(1,len(nums)+1))
        set_nums = set(nums)
        return list(set_result-set_nums)
                