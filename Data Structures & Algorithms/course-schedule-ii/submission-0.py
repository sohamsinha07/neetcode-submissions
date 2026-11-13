class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #build an adjacency list with the prereqs
        prereq = {}
        for c in range(numCourses):
            prereq[c] = []
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        #each course has 3 states
        # visited
        # visitng
        # univisited
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False: #cycle deteced
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output