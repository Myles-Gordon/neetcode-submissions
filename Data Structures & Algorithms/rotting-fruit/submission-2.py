class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [1,0], [-1, 0], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        count = 0
        fresh = 0
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh +=1

        while fresh > 0 and q: 
            infected = False
            for _ in range(len(q)):
                curR, curC = q.popleft()
                for dr, dc in directions:
                    newR = curR+dr
                    newC = curC+dc
                    if newR >= 0 and newR < rows and newC >= 0 and newC < cols and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        q.append((newR, newC))
                        fresh-=1
                        infected = True
            if infected: count+=1

        if fresh == 0:
            return count
        else:
            return -1
