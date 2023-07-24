from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True

        requirements = defaultdict(list)
        for course, pre_course in prerequisites:
            requirements[course].append(pre_course)

        def dfs_deadlock(idx):
            if status[idx] != 0:
                return status[idx] == 1
            
            status[idx] = 1

            for pre_course in requirements[idx]:
                if dfs_deadlock(pre_course):
                    return True
                    
            status[idx] = 2
            return False

        status = [0]*numCourses

        for idx in range(numCourses):
            if dfs_deadlock(idx):
                return False


        return True