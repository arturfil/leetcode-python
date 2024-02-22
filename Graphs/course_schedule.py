from typing import List

class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        courses = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            courses[a].append(b)

        for node in range(numCourses):
            if not self.dfs(node, visiting, courses):
                return False
        return True

    # we do dfs because we want to know if we can finish
    def dfs(self, node, visiting, courses):
        if node in visiting: # cycle
            return False
        if courses[node] == []: # if empty means no reqs
            return True
        
        visiting.add(node)

        for pre in courses[node]:
            if not self.dfs(pre, visiting, courses): # cycle
                return False

        visiting.remove(node) # remove visiting

        courses[node] = [] # no cycle, doable
        return True
