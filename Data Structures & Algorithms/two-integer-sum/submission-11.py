class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            newT = target-nums[i]
            if newT in nums[i+1:]:
                return [i, nums.index(newT, i+1)]