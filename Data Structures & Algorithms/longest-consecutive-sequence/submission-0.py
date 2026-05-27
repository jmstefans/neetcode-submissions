class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # initialize to longestSequence to handle len(nums) == 0
        longestSequence = 0

        # put nums in a set
        seqSet = set(nums)

        # loop through nums
        for i in range (0, len(nums)):

            # if left neighbor doesn't exist
            if nums[i] - 1 not in seqSet:

                # loop through i + 1 until we don't have sequence and update longestSequence
                temp = nums[i] + 1
                count = 1
                while (temp in seqSet):
                    temp += 1
                    count += 1

                if count > longestSequence:
                    longestSequence = count

            # else ignore non-sequece starters

        return longestSequence










        # we can try to identify starts of sequences by checking if the difference between values
        # we've already seen is greater than the length of the input array nums.

        # In example 1 [2,20,4,10,3,4,5] we could put 2 in an array then since we see that 20 is 
        # 18 away from 2 and nums length is 7 that it can't be part of the first sequence so we
        # can maybe put it in a second array.

        # Problem might be with this approach is that if the 3rd number is within distance of being
        # in both sequences should it go in both sequence arrays? Maybe yes and there is no problem 
        # after all?