class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """we can index the items in the array
        have a monotonically decreasing stack,
        once we reach a number greater than that
        each number is given the difference in indeces if popped
        start with all 0 so only change the ones that get popped"""
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                x, y = stack.pop()
                res[y] = abs(y - i)
            
            stack.append([t, i])

        return res

        