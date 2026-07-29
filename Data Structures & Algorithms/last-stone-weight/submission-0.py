class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        while len(stones) > 1:
            heapq.heapify(stones)
            new = heapq.heappop(stones) - heapq.heappop(stones)
            if new != 0:
                heapq.heappush(stones, new)
        
        return -stones[0] if stones else 0