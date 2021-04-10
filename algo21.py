# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            new_node = ListNode(l1.val)
            l1 = l1.next
        else:
            new_node = ListNode(l2.val)
            l2 = l2.next
        node = new_node
        while l1 and l2:
            if l1.val < l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            node.next = ListNode(val)
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return new_node