# https://leetcode.com/problems/course-schedule/

def canFinish(numCourses, prerequisites):
    n = numCourses
    adjList = [[] for _ in range(n)]
    for (c1, c2) in prerequisites:
        adjList[c2].append(c1)

    state = [0] * n
    
    def hasCycle(v):
        if state[v] == 1:
            return False 
        if state[v] == -1:
            return True
        state[v] = -1
        for i in adjList[v]:
            if hasCycle(i):
                return True

        state[v] = 1
        return False

    for v in range(n):
        if hasCycle(v):
            return False
        
    return True