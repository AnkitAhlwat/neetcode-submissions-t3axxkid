class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,v in enumerate(nums):
            if v > 0:
                break
            if len(res) > 0 and res[-1][0] == v:
                continue
            l,r = i+1, len(nums) -1 
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0: 
                    r-=1
                if total < 0:
                    l+=1
                if total == 0: 
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1

        return res
            
                
            