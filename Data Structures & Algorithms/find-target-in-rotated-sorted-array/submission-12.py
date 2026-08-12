class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """if l, r is sorted, if m greater than target
        r = m - 1, if m less than target, l = m + 1
        once l = r we can return -1, else if m = target return m
        
        if l,r is not sorted, if m greater than r, split is to
        the right of m, if target greater than m or less
        than l, l = m + 1 if target less than m and geq to l
        r = m - 1, if target less than r, l = m + 1
        """
        n = len(nums)
        l, r= 0, n - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            else:
                if nums[l] <= nums[r]:
                # sorted
                    if nums[m] > target:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if nums[m] > nums[r]:
                        #split is to the rightg of m
                        #consider cases where we move l to right of m
                        # if target less than l
                        # if target greater than m
                        if target < nums[l] or target > nums[m]:
                            l = m + 1
                        #consider cases where move r to left of m
                        # if target less than m and geq to l
                        elif nums[l] <= target < nums[m]:
                            r = m - 1
                    elif nums[m] < nums[r]:
                        #split is to the left of m
                        #consider cases where we move l to right of m
                        #if target greater than m and leq r
                        if nums[m] < target <= nums[r]:
                            l = m + 1
                        #consider cases r = m -1
                        #if target greater than nums[r] or less than nums[m]
                        elif target > nums[r] or target < nums[m]:
                            r = m - 1

            
        return -1

            
