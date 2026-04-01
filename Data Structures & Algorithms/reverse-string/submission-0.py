class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s) - 1
        l, r = 0, n
        while l <= r:
            s[r], s[l] = s[l], s[r]
            l += 1
            r -=1
        
        """
        Do not return anything, modify s in-place instead.
        """
        