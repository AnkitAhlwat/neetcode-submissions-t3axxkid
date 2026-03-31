class Solution:
    # Counting sort O(N + K)
    def counting_sort_letters(self,array):
        count = [0] * 26
        for char in array:
            if char.isalpha():
                index = ord(char.lower()) - ord("a")
                count[index] +=1

        # Reconstruct array
        sorted_array = []
        for i in range(26):
            sorted_array.extend([chr(i+ord('a'))] * count[i])
        return "".join(sorted_array)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_hash_map = {}
        for index,word in enumerate(strs): 
            sorted_word = self.counting_sort_letters(word)
            if sorted_word not in new_hash_map:
                new_hash_map[sorted_word] = [word]
            else:
                new_hash_map[sorted_word].append(word)
        return list(new_hash_map.values())
                