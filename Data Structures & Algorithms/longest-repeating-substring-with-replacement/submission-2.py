class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        char_dict = {}
        for r in range(len(s)):
            if s[r] not in char_dict:
                char_dict[s[r]] = 1
            else:
                char_dict[s[r]] +=1
            max_value = sorted(char_dict.values(), reverse=True)[0]
            length = (r - l + 1) - max_value
            if length <=k:
                res = max(res,r-l+1)
            else:
                while length > k:
                    char_dict[s[l]] -=1
                    l+=1
                    max_value = sorted(char_dict.values(), reverse=True)[0]
                    length = (r - l + 1) - max_value
        return res
