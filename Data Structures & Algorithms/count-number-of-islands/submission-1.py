class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [-1, 0], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    curRow = row+dr
                    curCol = col+dc
                    if curRow < 0 or curRow>=rows or curCol<0 or curCol >= cols or grid[curRow][curCol] == "0":
                        continue
                    q.append((curRow,curCol))
                    grid[curRow][curCol] = "0"
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands+=1
        
        return islands
        