# https://leetcode.com/problems/squares-of-a-sorted-array/ Given an integer array nums sorted
# in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
# Time complexity: O(n)
# Tests runtime: 220ms (faster than 94%)
# Tests memory: 16mo (less than 60%)

class Solution:
    def sortedSquares(self, nums):
        i = 0
        j = len(nums) - 1
        sorted_squares = [0] * len(nums)
        for n in range(len(nums) - 1, -1, -1):
            square1 = nums[i] * nums[i]
            square2 = nums[j] * nums[j]
            if square1 > square2:
                sorted_squares[n] = square1
                i += 1
            else:
                sorted_squares[n] = square2
                j -= 1
        return sorted_squares
