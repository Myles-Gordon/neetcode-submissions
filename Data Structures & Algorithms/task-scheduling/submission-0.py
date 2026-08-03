class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [cnt for cnt in counts.values()]
        heapq.heapify_max(maxHeap)
        
        queue = deque()
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) - 1
                if cnt:
                    queue.append([cnt, time+n])
            
            if queue and queue[0][1] == time:
                heapq.heappush_max(maxHeap, queue.popleft()[0])

        return time