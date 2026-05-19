class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        
        for i in range(len(nums)):
            j = i + 1
            for j in range(j, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]