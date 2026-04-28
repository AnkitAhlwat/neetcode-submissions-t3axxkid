class Solution:
    def isValid(self, s: str) -> bool:
        char_mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for c in s:
            if c in char_mapping.keys():
                if not stack:
                    return False
                popped = stack.pop()
                if char_mapping[c] != popped:
                    return False
                continue
            stack.append(c)
            
        return len(stack) == 0