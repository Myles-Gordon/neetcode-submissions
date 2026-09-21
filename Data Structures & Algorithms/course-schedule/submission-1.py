class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependents = defaultdict(list)     # required machine -> machines waiting on it
        waiting_on = [0] * numCourses    # unmet requirements per machine

        for course, pre in prerequisites:
            dependents[pre].append(course)   # pre unlocks course
            waiting_on[course] += 1

        q = deque(m for m in range(numCourses) if waiting_on[m] == 0)
        started = 0
        while q:
            m = q.popleft()
            started += 1
            for d in dependents[m]:
                waiting_on[d] -= 1
                if waiting_on[d] == 0:
                    q.append(d)

        return started == numCourses