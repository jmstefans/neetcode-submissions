class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # use bucket sort for O(n) time and space complexity

        # make an array with the indices as the count/frequency of how many 
        # times an element shows up in the nums input list and the value would
        # be a list of all the elements that show up that many times
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res