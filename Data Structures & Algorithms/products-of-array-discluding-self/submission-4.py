class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            left[i] = prefix
            prefix *= nums[i] 

        right = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)-1,-1,-1):
            right[i] = prefix
            prefix *= nums[i]
        
        
        
        return list(map(lambda a,b: a*b,left,right))
        