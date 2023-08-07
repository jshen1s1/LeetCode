import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # add all start-events and end-events, then sort them in left to right order
        event = [(L, -H, R) for L, R, H in buildings]
        event += [(R, 0, 0) for _, R, _ in buildings]
        event.sort()

        # res: [(x, height)]
        # hp: [(-height, ending x)]
        res = [(0,0)]
        hp = [(0, float('inf'))]
        for pos, negH, end in event:
            # remove all passed buildings
            # if a start-event, add that building to hp
            # if prev height != current height, add to result
            while pos >= hp[0][1]:
                heapq.heappop(hp)
            if negH:
                heapq.heappush(hp, (negH, end))
            if res[-1][1] != -hp[0][0]:
                res.append((pos, -hp[0][0]))

        return res[1:]