from typing import Optional

from BinaryTree.tree_node import TreeNode


class InvertBinaryTree:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root not None:
            left = root.left  
            right = root.right
