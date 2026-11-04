class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r, c):
            q = deque()
            currMax = 1
            grid[r][c] = 0
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    elif grid[nr][nc] == 1:
                        currMax += 1
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return currMax


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    currArea = bfs(r, c)
                    maxArea = max(currArea, maxArea)
        return maxArea
