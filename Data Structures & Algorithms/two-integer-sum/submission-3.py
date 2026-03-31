class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for index,num in enumerate(nums):
            if (target - num) in hash_table:
                return [hash_table.pop(target-num),index]
            hash_table[num] = index