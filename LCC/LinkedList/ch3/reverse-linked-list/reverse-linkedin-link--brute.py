# https://leetcode.com/problems/reverse-linked-list
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class Solution:
    def reverseList(self, head):
        last_node = None
        while head is not None:
          new_node = ListNode(head.val, last_node)
          last_node = new_node
          head = head.next
        return last_node