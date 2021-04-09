# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
# Given an array nums of integers, return how many of them contain an even number of digits.
#
# Time complexity O(n)
# Tests runtime: 44ms (faster than 97%)
# Tests memory: 14mo (less than 42%)

class Solution:
    def findNumbers(self, nums):
        counter = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                counter += 1
        return counter
