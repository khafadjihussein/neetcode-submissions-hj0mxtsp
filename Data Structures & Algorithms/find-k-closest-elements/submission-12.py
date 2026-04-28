class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k - 1
        n = len(arr)

        while r < n - 1:
            left_dist = abs(arr[l] - x)
            next_dist = abs(arr[r + 1] - x)

            if next_dist < left_dist or (next_dist == left_dist and arr[r + 1] == arr[l]):
                l += 1
                r += 1
            else:
                break

        return arr[l:r + 1]