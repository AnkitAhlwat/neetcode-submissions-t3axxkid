class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(string)) + "#" + string for string in strs])

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            delimmter_index = index
            while s[delimmter_index] != '#':
                delimmter_index +=1
            length_of_word = int(s[index:delimmter_index])

            word = s[delimmter_index+1:delimmter_index+length_of_word+1]
            result.append(word)
            index = delimmter_index +1 + length_of_word
        return result