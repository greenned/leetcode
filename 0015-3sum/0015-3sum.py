class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 리스트를 정렬합니다.
        res = []

        for i in range(len(nums)):
            # 중복을 피하기 위해 이전 값과 동일한 경우 건너뜁니다.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]  # 두 숫자의 합이 이 값을 만족해야 합니다.
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # 중복을 피하기 위해 동일한 값을 건너뜁니다.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return res