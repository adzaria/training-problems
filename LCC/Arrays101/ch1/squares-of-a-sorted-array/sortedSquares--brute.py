# https://leetcode.com/problems/squares-of-a-sorted-array/ Given an integer array nums sorted
# in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
# Time complexity: O(n) for squares but more for the python sorted() function
# Tests runtime: 204ms (faster than 94%)
# Tests memory: 16mo (less than 60%)

class Solution:
    def sortedSquares(self, nums):
        return sorted([x * x for x in nums])
