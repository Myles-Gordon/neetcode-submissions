class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = max(piles)
        if len(piles) == h:
            return largest
    
        l = 1
        r = largest
        best = largest
        while l<=r:
            m = (r+l) // 2
            time = 0
            for b in piles:
                time += math.ceil(b / m)
            if time<=h:
                best = m
                r = m-1
            else:
                l = m+1
        
        return best

        