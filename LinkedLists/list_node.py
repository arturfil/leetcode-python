class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printNodes(self, node):
        while node:
            print(node.val)
            node = node.next
