class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        # maybe we just compare the l and r pointers to decide where to search?
        while l <= r:

            # if sorted then left value is equal or less than current min/result and stop looking
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])

            # search left or right?
            # if mid is part of the left sorted portion then search right
            if nums[m] >= nums[l]:
                l = m + 1
            else: # search left
                r = m - 1
        
        return res