class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack = []
        for c in s:
            if c not in hash_map:
                if len(stack) == 0:
                    return False
                if c == hash_map[stack.pop(-1)]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0