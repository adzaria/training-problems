# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/ Given an array of integers numbers that
# is already sorted in ascending order, find two numbers such that they add up to a specific target number. Return
# the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1]
# <= numbers.length. You may assume that each input would have exactly one solution and you may not use the same
# element twice.
#
# Runtime: 56ms (faster than 94%)
# Memory: 14mo (less than 31%)

class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            if numbers[i] + numbers[j] < target:
                i += 1
            if numbers[i] + numbers[j] > target:
                j -= 1
