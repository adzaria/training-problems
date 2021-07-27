# https://leetcode.com/problems/palindrome-linked-list
# Given the head of a singly linked list, return true if it is a palindrome.

class Solution:
    def isPalindrome(self, head) -> bool:

        vals = []
        while head is not None:
            vals.append(head.val)
            head = head.next

        for i in range(0, floor((len(vals)) / 2)):
            if vals[i] != vals[len(vals) - 1 - i]:
                return False
        return True