class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """check weight capacities from minimum to maximum,
        can binary search thru
        use a function that checks if its valid"""

        def check(x):
            currweight = 0
            n = len(weights)
            currdays = 1
            for i in range(n):
                if currweight + weights[i] > x:
                    currweight = weights[i]
                    currdays += 1
                    if currdays > days:
                        return False
                else:
                    currweight += weights[i]
            return True
        l, r = max(weights), sum(weights)
        while l<= r:
            m = (l+r)//2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l
            
                    

        