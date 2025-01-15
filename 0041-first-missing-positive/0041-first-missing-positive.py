class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hash_set = set()

        for num in nums:
            if num > 0:
                hash_set.add(num)

        for i in range(1, len(nums) + 2):
            if i not in hash_set:
                return i


        