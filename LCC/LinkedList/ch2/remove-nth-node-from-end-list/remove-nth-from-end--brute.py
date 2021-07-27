# https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        while head is not None:
          nodes.append(head)
          head = head.next
        nodes.pop(len(nodes) - n)
        print(len(nodes))
        if(len(nodes) == 0):
          return None
        if(len(nodes) == 1):
          nodes[0].next = None
          return nodes[0]
        new_head = nodes[0]
        new_head.next = None
        for i in (range(0, len(nodes) - 1)):
          nodes[i].next = nodes[i+1]
          nodes[i+1].next = None
        return new_head