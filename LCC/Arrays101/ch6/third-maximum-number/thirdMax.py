# https://leetcode.com/problems/third-maximum-number Given integer array nums, return the third maximum number in
# this array. If the third maximum does not exist, return the maximum number.
#
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def thirdMax(self, nums):

        three_maximums = set()

        for i in range(len(nums)):
            three_maximums.add(nums[i])
            if len(three_maximums) > 3:
                three_maximums.remove(min(three_maximums))

        if len(three_maximums) == 3:
            return min(three_maximums)

        return max(three_maximums)
