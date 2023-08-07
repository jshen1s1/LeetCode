class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        xOverlap = min(ax2, bx2) - max(ax1, bx1)
        yOverlap = min(ay2, by2) - max(ay1, by1)

        if xOverlap <= 0 or yOverlap <= 0:
            return abs(ax1 - ax2) * abs(ay1 - ay2) + abs(bx1 - bx2) * abs(by1 - by2)
        else:
            
            return abs(ax1 - ax2) * abs(ay1 - ay2) + abs(bx1 - bx2) * abs(by1 - by2) - xOverlap * yOverlap