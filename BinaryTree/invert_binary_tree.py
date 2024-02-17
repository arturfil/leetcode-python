from typing import Optional
from BinaryTree.tree_node import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root != None:

            left, right = root.left, root.right

            root.left = self.invertTree(right)
            root.right = self.invertTree(left)

        return root

