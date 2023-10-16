import heapq as hp

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        hp.heappush(self.small, -num)
        hp.heappush(self.large, -self.small[0])
        hp.heappop(self.small)

        if len(self.small) < len(self.large):
            hp.heappush(self.small, -self.large[0])
            hp.heappop(self.large)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()