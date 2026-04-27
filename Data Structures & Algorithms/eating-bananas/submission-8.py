class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # upper bound of k is the max integer in pile such that u take n hours to eat
        # lower bound of k is 1, can compute the hours taken by doing ceil[piles[i] / k]
        # if hours taken is equal below h it is valid but not optimal (this is now l), if above h not valid, do r - 1
        import math
        n = len(piles)
        l, r = 1, max(piles)
        while l < r:
            m = (l+r) // 2
            time = 0
            for i in piles:
                time +=  math.ceil(i/m)
            if time <= h:
                r = m
            else:
                l = m + 1
        return r

        