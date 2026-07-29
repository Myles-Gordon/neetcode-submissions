class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hm = defaultdict(list)
        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            hm[dist].append(p)
        
        dists = list(hm.keys())
        heapq.heapify(dists)
        res = []
        while len(res) < k:
            for p in hm[heapq.heappop(dists)]:
                res.append(p)
        return res