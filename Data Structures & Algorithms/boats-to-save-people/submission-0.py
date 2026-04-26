class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        l, r = 0, n - 1
        res = n
        while l < r:
            if people[l] + people[r] <= limit:
                res -= 1
                l += 1
                r -= 1
            elif people[l] + people[r] > limit:
                r -= 1
        return res
    
        