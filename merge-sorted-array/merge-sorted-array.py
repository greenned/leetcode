class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        pointer = 0
        while nums2:
            if nums2[0] <= nums1[pointer] or pointer >= m:
                nums1.pop(-1)
                nums1.insert(pointer, nums2.pop(0))
                pointer = 0
                m+=1
            # elif pointer >= m:
            #     nums1.pop(-1)
            #     nums1.insert(pointer, nums2.pop(0))
            #     m+=1
            else:
                pointer += 1
