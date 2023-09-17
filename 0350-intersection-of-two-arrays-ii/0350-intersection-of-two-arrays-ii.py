class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for num1 in nums1:
            if num1 in nums2:
                intersection.append(nums2.pop(nums2.index(num1)))
        return intersection
        