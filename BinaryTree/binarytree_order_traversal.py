import collections
from typing import Optional, List
from BinaryTree.tree_node import TreeNode

class BTOrderTraversal:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
        
'''
    # Testing
    head = treenode(1) 
    head.left = treenode(9)
    head.right = treenode(20)
    head.right.left = treenode(15)
    head.right.right = treenode(7)

    bt_traversal = btordertraversal()
    print(bt_traversal.level_order(head))

'''
