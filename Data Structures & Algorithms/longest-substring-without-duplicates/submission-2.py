class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # question about case being considered duplicate or not but will assume x and X not duplicates
        # need base case for s length 0 and 1 
        # otherwise, left pointer starts at 0 and right pointer starts at 1 
        # use hashmap to store character and its index so we can tell if we've seen this before 
        # and if so we can move the left pointer to 1 + that index
        # keep a counter for longest length

        if len(s) < 2:
            return len(s)

        result = 1
        l, r = 0, 1
        hashmap = {s[0] : 0}

        while r < len(s):
            if s[r] in hashmap:
                l = max(l, hashmap[s[r]] + 1)
            hashmap[s[r]] = r

            if r - l + 1 > result:
                result = r - l + 1

            r += 1

        return result