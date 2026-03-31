class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] +=1

                
            if tuple(count) not in anagramDict:
                anagramDict[tuple(count)] = []
            anagramDict[tuple(count)].append(s)
            

        return list(anagramDict.values())
