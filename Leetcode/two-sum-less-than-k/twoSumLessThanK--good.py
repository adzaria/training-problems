# https://leetcode.com/problems/two-sum-less-than-k/ Given an array nums of integers and integer k, return the
# maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this
# equation, return -1.
#
# Runtime: 32ms (faster than 99%)
# Memory: 14mb (less than 94%)

class Solution:
    def twoSumLessThanK(self, nums, k):
        max_found = -1
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            sum = nums[i] + nums[j]

            if k > sum > max_found:
                max_found = sum
                i += 1
                continue

            if sum > max_found:
                j -= 1
                continue
            if sum > k:
                break

            i += 1
        return max_found
