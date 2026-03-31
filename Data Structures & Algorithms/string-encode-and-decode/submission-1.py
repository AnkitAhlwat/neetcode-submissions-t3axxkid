class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for c in strs:
            encoded_str += str(len(c)) + "#" + c
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        index = 0
        while index < len(s):
            j = index
            while s[j] != "#":
                j+=1
            length = int(s[index:j])
            decoded_strs.append(s[j+1:j+1+length])
            index = j+1+length

        return decoded_strs