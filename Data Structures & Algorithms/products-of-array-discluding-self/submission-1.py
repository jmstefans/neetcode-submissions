class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        # productOfAll = 1
        # zero_count = nums.count(0)
        
        # if zero_count > 1:
            # return [0] * len(nums)
            
        # for i in nums:
            # if i != 0:
                # productOfAll *= i

        # Now that we have the product of all of the elements of the array
        # lets create the result array by dividing each element as we go
        # result = [0] * len(nums)
        # for i in range(len(nums)):
            # if zero_count == 1:
                # result[i] = productOfAll if nums[i] == 0 else 0 # protect against dividing by zero
            # else:
                # result[i] = int(productOfAll / nums[i]) # protect against floats as we want ints returned
        
        # return result