from typing import Optional
from LinkedLists.list_node import ListNode

class ReverseLinkedList:
    def reverse_list(self, head:Optional[ListNode]) -> Optional[ListNode]:
        previous = None

        while head != None:
            temp = head.next
            head.next = previous
            previous = head
            head = temp

        return head
