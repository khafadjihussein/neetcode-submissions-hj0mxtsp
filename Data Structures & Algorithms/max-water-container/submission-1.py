class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """area  is minheight of 2 selected bars times distance between them"""
        n = len(heights)
        l, r = 0, n-1
        res = 0
        while l < r:
            area = (min(heights[l], heights[r]))*(r-l)
            res = max(area, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
        