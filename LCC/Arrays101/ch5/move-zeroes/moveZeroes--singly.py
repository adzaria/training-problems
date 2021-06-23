# https://leetcode.com/problems/move-zeroes Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy
# of the array.
#
# Time complexity: O(n)
# Space complexity: O(1)
# Tests runtime: 44ms (faster than 91%)
# Tests memory: 15mo (less than 25%)

class Solution:
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        if i <= len(nums) - 1:
            for k in range(i, len(nums)):
                nums[k] = 0
