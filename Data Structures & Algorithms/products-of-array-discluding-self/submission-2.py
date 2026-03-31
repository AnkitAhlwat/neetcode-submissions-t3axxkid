class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        right = [1] * len(nums)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            right[i] = postfix
            postfix *= nums[i]
        for i in range(len(res)):
            res[i] = right[i] * res[i]

        return res
        