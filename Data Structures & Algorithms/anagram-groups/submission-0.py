class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap for anagrams with key being array of character counts and 
        # values being the various manifestations of the anagrams that go together
        allStringsHashmap = defaultdict(list)
        
        # loop through all strings
        for string in strs:

            # create an array for the current string
            curStringArray = [0] * 26 # a, b, .., z

            # loop through all characters and create the string's character count array
            for char in string:
                index = ord(char) - ord("a")
                curStringArray[index] += 1

            # add the current string's array and string to the anagrams hashmap if it doesn't
            # exist otherwise add the string
            allStringsHashmap[tuple(curStringArray)].append(string)

        # return output in desired format
        return list(allStringsHashmap.values())