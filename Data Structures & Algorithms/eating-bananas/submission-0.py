import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1 
        end = max(piles)
        minRate = end

        while start <= end:
            k = start + (end-start)//2
            time = sum([math.ceil(x/k) for x in piles])

            if time > h:
                start = k + 1
            else:
                minRate = min(k,minRate)
                end = k - 1
        return minRate