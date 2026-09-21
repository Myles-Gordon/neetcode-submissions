class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totals = [0] * (len(cost)+1)
        totals[len(cost)-1] = cost[len(cost)-1]

        for i in range(len(cost)-2, -1, -1):
            totals[i] = min(cost[i] + totals[i+1], cost[i] + totals[i+2])

        return min(totals[0], totals[1])