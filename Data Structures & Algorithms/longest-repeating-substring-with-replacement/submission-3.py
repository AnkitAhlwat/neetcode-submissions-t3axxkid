class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        char_dict = {}
        for r in range(len(s)):
            char_dict[s[r]] = 1 + char_dict.get(s[r],0)

            while (r-l+1) - max(char_dict.values()) > k:
                char_dict[s[l]] -=1
                l+=1
            res = max(res,(r-l+1))
        return res