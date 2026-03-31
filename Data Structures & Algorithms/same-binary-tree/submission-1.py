# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        que = deque()
        que_two = deque()

        que.append(p)
        que_two.append(q)

        while que or que_two:
            nodeP = que.popleft()
            nodeQ = que_two.popleft()

            if nodeP is None and nodeQ is None:
                continue
            if nodeP is None or nodeQ is None:
                return False
            if nodeP.val != nodeQ.val:
                return False

            que.append(nodeP.left)
            que.append(nodeP.right)
            que_two.append(nodeQ.left)
            que_two.append(nodeQ.right)

        return True

            