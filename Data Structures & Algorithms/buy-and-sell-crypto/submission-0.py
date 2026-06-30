class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # base case of prices.length == 1 should return 0 since we don't have two different days
        if len(prices) == 1:
            return 0

        # real algorithm with sliding window
        maxProfit = 0
        
        # start with l = 0 r = 1 and guess we need a base case for prices.length == 1
        l, r = 0, 1

        while r < len(prices):

            # if r < l then l = r and r += 1
            if prices[r] < prices[l]:
                l = r

            # else check if profit is greater than maxProfit and update
            else:
                profit = prices[r] - prices[l] 
                if profit > maxProfit:
                    maxProfit = profit
            
            # move right pointer at the end of every check
            r += 1

        return maxProfit
        
        # move r to the rigth by 1 and keep track of max price we see's index
        # maybe stop moving r if the next value is less than r?
        # in that case we move l 
        # brute force is too slow as it would be O(n^2)