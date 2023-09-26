from typing import Optional
from LinkedLists.listnode import ListNode

class LinkedListCycle:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next == None and head.next.next == None:
            return False

        slow = head.next
        fast = head.next.next

        while slow != fast:
            if fast.next == None and fast.next.next == None:
                return False
            slow = slow.next 
            fast = fast.next.next

        return slow == fast