class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        
        limit = 0
        
        while len(nums) > limit:
            sum_ = 0
            for idx, num in enumerate(nums):
                sum_ += num
                
                if idx == limit:
                    result.append(sum_)
                    limit += 1
                    break    
            
        return result
            