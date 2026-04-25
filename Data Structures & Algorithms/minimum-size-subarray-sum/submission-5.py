class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # have a left and right pointer
        # while above target decrement left, else increase right
        l = 0
        n = len(nums)
        res, currsum = float('inf'), 0
        for r in range(n):
            currsum += nums[r]
            while target <= currsum:
                length = r - l + 1
                res = min(res, length)
                currsum -= nums[l]
                l += 1
            
        if l == 0:
            return 0
        return res
                
        