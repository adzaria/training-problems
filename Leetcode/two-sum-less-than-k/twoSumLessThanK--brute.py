# https://leetcode.com/problems/two-sum-less-than-k/ Given an array nums of integers and integer k, return the
# maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this
# equation, return -1.
#
# Runtime: 96ms (faster than 9%)
# Memory: 14mb (less than 94%)

class Solution:
    def twoSumLessThanK(self, nums, k):
        maximum_sum = -1
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i >= j:
                    continue
                if num1 + num2 >= k or num1 + num2 < maximum_sum:
                    continue
                maximum_sum = num1 + num2
        return maximum_sum
