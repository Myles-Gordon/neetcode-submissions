class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dict = {}

        for x in nums:
            count = dict.get(x)
            if count:
                count+=1
                dict.update({x:count})
            else:
                dict.update({x:1})

        return len(dict)!=len(nums)
