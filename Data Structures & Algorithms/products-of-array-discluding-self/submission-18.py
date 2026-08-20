class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*(n+1)
        suffix = [1]*(n+1)
        res = [1]*n
        """n is length of array, index goes from 0 to n - 1
        prefix must have a 1 to the beginning
        suffix 1 after the end
        both have length n + 1
        iterate prefix starting from 1
        prefix[i] = nums[i]*prefix[i-1] up to n so range n + 1 (0)
        suffix[i] = nums[i]*suffix[i+1] from index n to 0 so (n, -1, -1)"""
        for i in range(1, n+1):
            prefix[i] = nums[i-1]*prefix[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1]*suffix[i+1]
        for i in range(n):
            res[i] = prefix[i]*suffix[i]
        return res
        