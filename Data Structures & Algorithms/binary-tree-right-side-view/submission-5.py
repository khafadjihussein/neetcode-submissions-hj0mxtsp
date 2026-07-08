# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #change bfs to only include node.right
        q = collections.deque()
        res = []
        q.append(root)
        while q:
            lenq = len(q)
            level = []
            for i in range(lenq):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
                

            if level:
                res.append(level)
        res1 = []
        for i in res:
            res1.append(i[-1])
        return res1

        