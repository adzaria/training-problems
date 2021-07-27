# https://leetcode.com/problems/remove-linked-list-elements Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val, and return the new head.

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def removeElements(self, head, val):
        vals = []
        while head is not None:
            if head.val != val:
                vals.append(head.val)
            head = head.next

        if (len(vals) == 0):
            return

        new_head = ListNode(vals[len(vals) - 1], None)
        for i in reversed(range(0, len(vals) - 1)):
            new_node = ListNode(vals[i], new_head)
            new_head = new_node
        return new_head