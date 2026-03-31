class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        longest_length = 0
        l,r = 0,0
        char_dict = set()
        while r < len(s):
            if s[r] in char_dict:
                while s[r] in char_dict:
                    char_dict.remove(s[l])
                    l+=1
            char_dict.add(s[r])
            length = r - l +1
            longest_length = max(longest_length,length)
            r+=1
        return longest_length
