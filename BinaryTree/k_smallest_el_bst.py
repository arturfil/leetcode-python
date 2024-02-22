from typing import Optional
from BinaryTree.tree_node import TreeNode

class KSmallestElInBst:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack, curr = [], root

        while stack or curr:
            while curr:
                stack.append(curr) # add to stack, traverse in order
                curr = curr.left # travel left first
            curr = stack.pop() # curr = to left most
            k -= 1 # reduce k every time you git a left bound
            if k == 0:
                return curr.val
            curr = curr.right # once you finish, travel right bound until k == 0

    def inorder(self, r):
        return self.inorder(r.left) + [r.val] + self.inorder(r.right) if r else []


    





             
