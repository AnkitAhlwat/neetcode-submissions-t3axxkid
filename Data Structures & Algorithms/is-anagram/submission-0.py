class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_hash = {}
        for letter in s:
            if letter not in first_hash:
                first_hash[letter] = 1
            else:
                first_hash[letter] +=1

        for letter in t:
            if letter not in first_hash:
                return False
            else:
                if first_hash[letter] == 1:
                    first_hash.pop(letter)
                elif first_hash[letter] > 0:
                    first_hash[letter] -= 1
        return len(first_hash) == 0
