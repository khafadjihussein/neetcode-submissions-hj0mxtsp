class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l<=r:
            m = (l+r)//2
            s = m*m
            if s == x:
                return m
            elif s < x:
                l = m + 1
            else:
                r = m - 1
        return r
        