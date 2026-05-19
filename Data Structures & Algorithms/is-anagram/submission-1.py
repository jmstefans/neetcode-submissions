class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdictionary, tdictionary = {}, {}

        for i in range(len(s)):
            sdictionary[s[i]] = 1 + sdictionary.get(s[i], 0) # Gets the value but if it doesn't exist gets a 0 to avoid an error.
            tdictionary[t[i]] = 1 + tdictionary.get(t[i], 0)
        
        for c in sdictionary:
            if sdictionary[c] != tdictionary.get(c, 0):
                return False

        return True