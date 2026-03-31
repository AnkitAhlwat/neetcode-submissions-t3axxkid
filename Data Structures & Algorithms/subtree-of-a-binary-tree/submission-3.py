# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        def sameTree(root,sub):
            s = []
            s.append((root,sub))
            while s:
                p,q = s.pop()
                if p is None and q is None:
                    continue
                if p is None or q is None:
                    return False
                if p.val != q.val:
                    return False
                s.append((p.left,q.left))
                s.append((p.right,q.right))
            return True


        if subRoot is None:
            return True
        stack = []
        stack.append(root)
        while stack:
                node = stack.pop()
                if node:
                    if node.val == subRoot.val and sameTree(node,subRoot):
                        return True
                    stack.append(node.left)
                    stack.append(node.right)
        return False
                
                

