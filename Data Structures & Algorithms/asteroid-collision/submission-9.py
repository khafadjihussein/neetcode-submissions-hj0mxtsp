class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """ use a stack, the latest positive value will colide with the 
        next neg value"""
        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            elif i < 0:
                if not stack or stack[-1] < 0:
                    stack.append(i)
                elif abs(stack[-1]) > abs(i):
                    continue
                elif abs(stack[-1]) == abs(i):
                    stack.pop()
                else:
                    while stack and stack[-1]> 0 and abs(stack[-1]) < abs(i):
                        
                        stack.pop()
                    
                    if not stack or stack[-1] < 0:
                        stack.append(i)
                    elif abs(stack[-1]) == abs(i):
                        stack.pop()
                        continue
                    elif abs(stack[-1]) > abs(i):
                        continue 
        return stack

        