# https://leetcode.com/problems/intersection-of-two-linked-lists
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
# It is guaranteed that there are no cycles anywhere in the entire linked structure.

class Solution:
    def getIntersectionNode(self, headA, headB):
      nodes = set()
      while (headA is not None) or (headB is not None):
        if headA in nodes:
          return headA
        if headB in nodes:
          return headB
        if headA == headB:
          return headA
        if headA is not None:
          nodes.add(headA)
          headA = headA.next
        if headB is not None:
          nodes.add(headB)
          headB = headB.next

