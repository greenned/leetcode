class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        diff_map = {}

        for i, val in enumerate(nums):
            diff = target - val

            if diff in diff_map:
                result.append(i)
                result.append(diff_map[diff])
                # return [diff_map[diff], i]
            diff_map[val] = i
        return result

