from typing import Optional
from tree_node import TreeNode

class SameTree:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False

        if p.left == q.left:
            self.isSameTree(p.left, q.left)
        else:
            return False

        if p.right == q.right:
            self.isSameTree(p.right, q.right)
        else:
            return False
