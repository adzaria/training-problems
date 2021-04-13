# https://leetcode.com/problems/max-consecutive-ones
# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Time complexity: O(n)
# Runtime: 344ms (faster than 77%)
# Memory: 14mo (less than 91%)

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_number = 0
        current_max = 0
        for num in nums:
            if num == 0:
                current_max = 0
                continue
            current_max += 1
            if max_number < current_max:
                max_number = current_max
        return max_number
