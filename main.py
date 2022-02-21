from LinkedLists.listnode import ListNode
from Recursion.merge_two_sortedLists import MergeTwoLSortedLists

def main():
    # Create linked list A
    head1 = ListNode(1)
    node1A = ListNode(2)
    node2A = ListNode(4)
    # Create linked list B
    head2 = ListNode(1)
    node1B = ListNode(2)
    node2B = ListNode(3)
    # Add next references to both linked lists
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

if __name__ == "__main__":
    main()