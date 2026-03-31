class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(string)) + "#" + string for string in strs])

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            length_of_word = int(s[i:j])
            i = j +1
            j += length_of_word +1
            result.append(s[i:j])

            i = j
        return result