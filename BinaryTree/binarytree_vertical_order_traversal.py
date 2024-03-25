from collections import defaultdict, deque
from typing import List, Optional
from BinaryTree.tree_node import TreeNode

class BTreeVerticalOrderTraversal:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                        
        return [columnTable[x] for x in sorted(columnTable.keys())]
