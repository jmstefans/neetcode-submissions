class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c not in dictionary:
                stack.append(c)
            elif stack: 
                    temp = stack.pop()
                    if dictionary.get(c) != temp:
                        return False
            else:
                return False

        if stack:
            return False
        else:
            return True