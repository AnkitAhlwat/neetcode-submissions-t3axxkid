from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
       
        def two_sum(start, target_val, first_num):
            l, r = start, len(nums) - 1
            
            while l < r:
                current_sum = nums[l] + nums[r]
                
                if current_sum == target_val:
                    res.add((first_num, nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif current_sum < target_val:
                    l +=1
                else:
                    r -=1

        for i in range(len(nums)):
            two_sum(i + 1, -nums[i], nums[i])

        return [list(v) for v in res]