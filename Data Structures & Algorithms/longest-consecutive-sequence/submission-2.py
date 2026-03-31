class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        largest_count = 0

        for num in nums:
            if (num -1 ) not in hash_set:
                length = 1
                while (num + length) in hash_set:
                    length +=1
                largest_count = max(largest_count,length)
        return largest_count
                