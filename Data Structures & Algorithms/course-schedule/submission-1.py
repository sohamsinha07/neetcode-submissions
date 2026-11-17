class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        for i in range(numCourses):
            prereq[i] = []
        for course, pre in prerequisites:
            prereq[course].append(pre)

        visited = set()
        def dfs(course):
            #want to check if this course has already been visited then it is a cycle
            if course in visited:
                return False
            if prereq[course] == []:
                return True
            visited.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False
            visited.remove(course)
            prereq[course] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
