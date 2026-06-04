class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the inputer array so that we can check left neighbor being the same value and skip if so
        # all positive values can be skipped since they won't sum to zero
        # it's basically 2 sum problem with j and k being a left and right pointer since i index is fixed
        # don't reuse duplicates (left neighbor is same value) when adjusting j and k too
        res = []
        nums.sort()

        for i, value in enumerate(nums):
            if i > 0 and value == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res












#        result = []
#        absValues = []

#        numsLength = len(nums)
        
#        for i in range(numsLength):
#            for j in range(i+1, numsLength):
#                for k in range(j+1, numsLength):
                    
                    # only interested in sums of 0
#                    if nums[i] + nums[j] + nums[k] != 0:
#                        continue

                    # abs val didn't work so maybe ordinal then sum 
                        # no ordinal won't work for negative values as they're 2 characters

                    # rearrange them in every order to see if any permutation matches?
                        # seems expensive

                    # sum is 0, so add to datastructure if not already there regardless of order
#                    absSum = abs(nums[i]) + abs(nums[j]) + abs(nums[k])
#                    if absSum not in absValues:
#                        absValues.append(absSum)
#                        result.append([nums[i], nums[j], nums[k]])

#        return result