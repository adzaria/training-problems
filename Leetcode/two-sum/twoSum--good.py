# https://leetcode.com/problems/two-sum/ Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target. You may assume that each input would have exactly one solution,
# and you may not use the same element twice. You can return the answer in any order.
#
# Runtime: 44ms (faster than 82%)
# Memory: 14mb (less than 72%)

class Solution:
    def twoSum(self, nums, target):
        remains_map = {}
        for i, num in enumerate(nums):
            if num in remains_map:
                return [i, remains_map[num]]
            remains_map.update({target - num: i})
