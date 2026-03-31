class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_elements = {}
        for num in nums:
            if num not in frequent_elements:
                frequent_elements[num] = 1
            else:
                frequent_elements[num] += 1
        count_of_elements = [[] for i in range(len(nums)+1)]
        for key,v in frequent_elements.items():
            count_of_elements[v].append(key)
        res = []
        print(count_of_elements)
        for count in range(len(count_of_elements)-1, 0, -1):
            for num in count_of_elements[count]:
                res.append(num)
                if len(res) == k:
                    return res
            

        return res
