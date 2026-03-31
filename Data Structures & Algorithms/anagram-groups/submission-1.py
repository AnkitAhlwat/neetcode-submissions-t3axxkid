class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}

        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string not in anagramDict:
                anagramDict[sorted_string] = []

            anagramDict[sorted_string].append(s)
        return list(anagramDict.values())
