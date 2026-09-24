class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependents = defaultdict(list)
        waiting = [0]*numCourses

        for course, pre in prerequisites:
            dependents[pre].append(course)
            waiting[course] +=1

        def bfs():
            visited = set()
            q = deque()
            for c in range(numCourses):
                if waiting[c] == 0:
                    q.append(c)
            
            while q:
                course = q.popleft()
                if course in visited:
                    return visited
                visited.add(course)
                unlocks = dependents[course]
                for c in unlocks:
                    waiting[c] -= 1
                    if waiting[c] == 0:
                        q.append(c)
            return visited
        
        v = bfs()
        return len(v) == numCourses