from typing import Optional
from BinaryTree.tree_node import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return None
        
        left = root.right
        right = root.left

        root.left = self.invertTree(left)
        root.right = self.invertTree(right)

        return root
        

             
