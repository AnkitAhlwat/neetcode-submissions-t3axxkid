class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        l,r = 0,0
        char_dict = {}
        while r < len(s):
            char_dict[s[r]] = 1 + char_dict.get(s[r],0)
            while (len(char_dict.values()) > 0) and ((r-l+1) - max(char_dict.values()) > k):
                print(r-l+1)
                print(max(char_dict.values()))
                print(char_dict.values())
                char_dict[s[l]]-=1
                l+=1
            result = max(result,r-l+1)
            r+=1
        return result