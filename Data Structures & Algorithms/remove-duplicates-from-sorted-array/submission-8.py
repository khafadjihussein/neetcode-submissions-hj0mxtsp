class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        seen = set()
        """ iterate thru array, if unique value update k and put it at index k"""
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
        