class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        pointer = 0
        
        while pointer < len(arr):
            if arr[pointer] == 0:
                arr.pop(-1)
                arr.insert(pointer, 0)
                pointer += 2
            else:
                pointer += 1