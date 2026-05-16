class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt, index = 1,0, -1
        for i in range(len(nums)):
            if nums[i]:
                prod *= nums[i]
            else:
                zero_cnt += 1
                index = i
        
        #Case 1: More than 1 zero
        if zero_cnt > 1:
            return [0]*len(nums)
        
        #Case 2: 1 zero
        if index != -1:
            output = [0]*len(nums)
            output[index] = prod
            return output
        
        #Case 3: No zeros
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] *= prod//nums[i]

        return output