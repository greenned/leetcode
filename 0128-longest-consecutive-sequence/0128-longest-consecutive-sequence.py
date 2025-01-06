class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:



        num_set = set(nums)
        longest = 0

        for num in num_set: # nums가 아닌 num_set임
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest