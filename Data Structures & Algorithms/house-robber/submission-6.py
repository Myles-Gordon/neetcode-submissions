class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        totals = [0] * len(nums)
        totals[0] = nums[0]
        totals[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            totals[i] = max(nums[i] + totals[i-2], totals[i-1])
        
        print(totals)
        return max(totals[len(nums)-1], totals[len(nums)-2])
