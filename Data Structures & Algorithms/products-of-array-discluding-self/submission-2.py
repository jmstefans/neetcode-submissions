class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1's.
        res = [1] * (len(nums))

        # Fill out the result array with the prefix products for every element.
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Update the result array with the product of the prefix for each element 
        # with the postfix product for each element.
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        # Return the result.
        return res


        # Easy way with no constraint on time and space.

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