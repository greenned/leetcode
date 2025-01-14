class MedianFinder:

    def __init__(self):
        self.stream = []
        

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.stream)
        
        while l < r:
            mid = (l+r) // 2
            if self.stream[mid] <  num:
                l = mid + 1
            else:
                r = mid
        self.stream.insert(l, num)


    def findMedian(self) -> float:
        if len(self.stream) % 2 == 0:
            mid_right = int(len(self.stream) / 2)
            mid_left = mid_right - 1
            return (self.stream[mid_left] + self.stream[mid_right])/ 2

        else:
            mid = len(self.stream) // 2
            return float(self.stream[mid])

        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()