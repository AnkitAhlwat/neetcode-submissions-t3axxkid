from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        def two_sum(start, target, first_val):
            l, r = start, n - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.add((first_val, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1

        for i in range(n):
            
            two_sum(i + 1, -nums[i], nums[i])

        return [list(t) for t in res]