class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        sorted_heights = sorted(heights)
        
        num = 0
        for origin, sort in zip(heights, sorted_heights):
            if origin != sort:
                num += 1
        return num
        