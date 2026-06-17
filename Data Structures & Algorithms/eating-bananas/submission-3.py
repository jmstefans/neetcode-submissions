class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum k eating rate is 1 i suppose
        # maximum k eating rate 1 billion from constraint? 

        # brute force by starting at 1 and incrementing by 1
        # would be O(h * n)?
        # would be going through positive ints potentially up to 1 billion but that's O(1) right?
        # or maybe O(5,000,000) on avg.
        # then trying that current positive int up to h times
        # so O(h) or O(5,000,000 * h)

        # could it be faster?
        # not sure how to relate that to O(n)
        
        # would sorting help?
        # ya because then we know our max pile size and no need to look at ints above the max
        # but can find max faster in linear O(n) time than sorting time O(nlogn)

        # our left and right are for the binary search for k (eating rates)
        r = max(piles)
        l = 1
        res = r

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
    
            # if this eating rate ate all of the bananas then we need to go smaller
            if hours <= h:
                res = min(res, m)
                r = m - 1
            #if self.test(piles, h, m):

            # else if this eating rate didn't finish all of the bananas then we need to increase the eating rate
            #elif self.test(piles, h, m):
            if hours > h:
                l = m + 1

        return res
            
    #def test(self, piles: List[int], h: int, k: int) -> bool:
        # go through each pile one at a time
     #   for i in range(h):
      #      pileIndex = 0
            # if there are some bananas in the pile, subtract k bananas
       #     if piles[pileIndex] > 0:
         #       piles[pileIndex] -= k
        #    else:
          #      pileIndex += 1

        # if the last pile is empty than this eating rate gets rid of all of the piles
        #return piles[len(piles) - 1] <= 0
