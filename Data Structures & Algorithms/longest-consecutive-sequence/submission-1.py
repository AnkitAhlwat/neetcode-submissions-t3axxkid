class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        largest_count = 0

        for num in nums:
            if (num-1) in hash_set:
                continue
            else:
                count = 1
                new_starting_num = num
                while new_starting_num + 1 in hash_set:
                    new_starting_num +=1
                    count +=1
                largest_count = max(largest_count,count)
        return largest_count
                