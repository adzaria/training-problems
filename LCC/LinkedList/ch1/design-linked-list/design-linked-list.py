# https://leetcode.com/problems/design-linked-list Design your implementation of the linked list. You can choose to
# use a singly or doubly linked list. A node in a singly linked list should have two attributes: val and next. val is
# the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly
# linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all
# nodes in the linked list are 0-indexed.
#
# Implement the MyLinkedList class:
#
# MyLinkedList() Initializes the MyLinkedList object. int get(int index) Get the value of the indexth node in the
# linked list. If the index is invalid, return -1. void addAtHead(int val) Add a node of value val before the first
# element of the linked list. After the insertion, the new node will be the first node of the linked list. void
# addAtTail(int val) Append a node of value val as the last element of the linked list. void addAtIndex(int index,
# int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the
# linked list, the node will be appended to the end of the linked list. If index is greater than the length,
# the node will not be inserted. void deleteAtIndex(int index) Delete the indexth node in the linked list,
# if the index is valid.
#
# Runtime: 384ms (faster than 16%)
# Memory: 14.8mo (less than 96.58%)
#
# First time I implement a linked list, it is messy as I changed a few things after writing it

class Node:
    def __init__(self, value, pointer_to):
        self.value = value
        self.next = pointer_to


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._sentinel = Node(None, None)
        self._length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current_node = self._sentinel.next
        for i in range(0, self._length):
            if i == index:
                return current_node.value
            current_node = current_node.next
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val, self._sentinel.next)
        self._sentinel.next = new_node
        self._length = self._length + 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if(self._length == 0):
          return self.addAtHead(val)
        current_node = self._sentinel.next
        new_node = Node(val, None)
        for i in range(0, self._length):
            if i == self._length - 1:
                current_node.next = new_node
                self._length = self._length + 1
                break
            else:
                current_node = current_node.next

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        current_node = self._sentinel
        new_node = Node(val, None)
        for i in range(0, self._length + 1):
            if i == index:
                new_node.next = current_node.next
                current_node.next = new_node
                self._length = self._length + 1
                break
            else:
                current_node = current_node.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        current_node = self._sentinel
        for i in range(0, self._length):
            if i == index:
                current_node.next = current_node.next.next
                self._length = self._length - 1
                break
            else:
                current_node = current_node.next
