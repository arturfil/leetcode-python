import math

from typing import Optional
from BinaryTree.tree_node import TreeNode

class ValidateBinaryTree:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)

    def validate(self, node, left=-math.inf, right=math.inf):
        if not node: return True 

        if node.val <= left or node.val >= right:
            return False

        return (self.validate(node.right, node.val, right) and 
                self.validate(node.left, left, node.val)) 

        '''
        For testing
        head = TreeNode(4)
        l1 = TreeNode(2)
        l2 = TreeNode(1)
        l3 = TreeNode(3)
        r1 = TreeNode(7)
        r2 = TreeNode(5)
        r3 = TreeNode(8)

        head.left = l1
        l1.left = l2
        l1.right = l3

        head.right = r1
        r1.left = r2
        r1.right = r3

        bt = ValidateBinaryTree()
        bt.isValidBST(head)

        '''
