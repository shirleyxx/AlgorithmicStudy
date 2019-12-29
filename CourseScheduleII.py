class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        def dfs(i):
            if visit[i] == 1: return True
            if visit[i] == 0: return False
            visit[i] = 0
            for pre in pres[i]:
                if not dfs(pre):
                    return False
            visit[i] = 1
            courses.insert(0,i)
            return True
        
        pres = [[] for i in range(numCourses)]
        for pair in prerequisites:
            pres[pair[1]].append(pair[0])
            
        courses = []
        visit = [-1 for i in range(numCourses)]
        for i in range(numCourses):
            if not dfs(i):
                return []
    
        
        return courses
