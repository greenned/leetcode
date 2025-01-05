class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        result = [0] * n

        left[0] = right[-1] = 1

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        for j in range(n-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]
        
        for k in range(n):
            result[k] = left[k] * right[k]
        return result
        