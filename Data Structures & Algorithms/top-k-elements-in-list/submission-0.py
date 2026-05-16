class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1+count.get(num,0)

        sorted_c = sorted(count.items(), key=lambda item: item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_c[i][0])

        return res