from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not prerequisites:
            return [i for i in range(numCourses)]

        req = defaultdict(list) # create a graph for all courses
        for course, prevCourse in prerequisites:
            req[course].append(prevCourse)

        def deadLock(idx):
            if status[idx] != 0:
                return status[idx] == 1
            
            status[idx] = 1

            for prevCourse in req[idx]:
                if deadLock(prevCourse):
                    return True
            
            status[idx] = 2
            if idx not in order: order.append(idx)
            return False
        
        order = []
        status = [0]*numCourses
        for i in range(numCourses):
            if deadLock(i):
                return []
        
        return order