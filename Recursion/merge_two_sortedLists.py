from typing import Optional
from LinkedLists.listnode import ListNode

class MergeTwoLSortedLists:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None :
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists( list1, list2.next)
            return list2

'''
    TESTING
    head1 = ListNode(1)
    node1A = ListNode(2)
    node2A = ListNode(4)

    head2 = ListNode(1)
    node1B = ListNode(2)
    node2B = ListNode(3)

    head1.next = node1A
    node1A.next = node2A

    head2.next = node1B
    node1B.next = node2B
    
    merge = MergeTwoLSortedLists()
    res = merge.mergeTwoLists(head1, head2)
    
    head1.printNodes(head1)
    print('---------------------')
    # in case the head node 2 is smaller
    head2.printNodes(head2)

    EXPLANATION
    - You want to check which node value is small, which ever
    is smaller, you assign .next to the what ever the function
    recursion returns with new values of that that node.next and
    the other node.
    - i.e nodeA(1) nodeB(5) -> nodeA.next = compare(nodeA.next, nodeB)
'''