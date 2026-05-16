class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            numTarget = target-num
            if numTarget == num and (nums.count(num)==2):
                ind = nums.index(num)
                for i in range(ind+1, len(nums), 1):
                    if nums[i] == num:
                        return [ind, i]
            if numTarget!=num and numTarget in nums:
                return [nums.index(num), nums.index(numTarget)]