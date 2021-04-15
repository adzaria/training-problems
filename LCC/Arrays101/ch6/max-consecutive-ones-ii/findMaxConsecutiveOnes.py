# https://leetcode.com/problems/max-consecutive-ones-ii/
# Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.
#
# Personal note: It took me too long to solve this but very pleasant, which is kind of simple in the end, it is just
# a moving frame.
#
# Time complexity: O(n)
# Space complexity: O(1)
# Tests runtime: 352ms (faster than 92%)
# Tests memory: 14mo (less than 51%)


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0
        max_ones_in_window = 0
        last_zero_index = -1
        does_list_contain_zero = False
        for i in range(len(nums)):
            if nums[i] == 1:
                max_ones_in_window += 1
                if max_ones_in_window > max_ones:
                    max_ones = max_ones_in_window
                continue
            # under here nums[i] == 0
            if not does_list_contain_zero:
                max_ones_in_window += 1
                last_zero_index = i
                does_list_contain_zero = True
                if max_ones_in_window > max_ones:
                    max_ones = max_ones_in_window
                continue
            if does_list_contain_zero:
                max_ones_in_window = i - (last_zero_index)
                last_zero_index = i
            if max_ones_in_window > max_ones:
                max_ones = max_ones_in_window
        return max_ones
