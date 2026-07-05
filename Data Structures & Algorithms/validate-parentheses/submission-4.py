class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for i in s:
            if i in key:
                if not stack:
                    return False
                if key[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack


        