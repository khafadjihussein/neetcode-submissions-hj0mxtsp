class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        """we need to find the split
        if r is less than l the split is in between them, otherwise l 
        is the min or left to l is the min, need to restrict our binary 
        search so we dont escape the window
        lets say the mid is less than r, we shift l to mid
        while r is less than l
        if mid and l in left sorted segment then min is to the right of 
        mid, make l mid + 1, if mid and r in right sorted segment"""
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[r]