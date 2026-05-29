class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use left and right pointer
        l, r = 0, len(numbers) - 1

        # while not found and pointers haven't reached each other yet (can't use same element twice)
        while l < r: # since always one valid solution then could just do while true and live dangerously..

            # sum
            sum = numbers[l] + numbers[r]

            # if found return 1-based pointers
            if sum == target:
                return [l + 1, r + 1]
                
            #if target is less than sum decrement right pointer
            if target < sum:
                r -= 1

            # if target is greater than sum increment left pointer
            if target > sum:
                l += 1