# https://leetcode.com/problems/valid-mountain-array
# Given an array of integers arr, return true if and only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
#   arr.length >= 3
#   There exists some i with 0 < i < arr.length - 1 such that:
#   arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#   arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
# Personal note: the code could be shorter, but time complexity is probably great
#
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def validMountainArray(self, arr):
        number_of_spears = 0
        number_of_valleys = 0
        if len(arr) < 3:
            return False
        for i in range(2, len(arr)):
            if arr[i-2] == arr[i-1] or arr[i-1] == arr[i]:
                return False
            if (arr[i - 2] < arr[i - 1]) and (arr[i] < arr[i - 1]):
                number_of_spears += 1
            if (arr[i - 2] > arr[i - 1]) and (arr[i] > arr[i - 1]):
                number_of_valleys += 1
        if number_of_spears == 1 and number_of_valleys == 0:
            return True
        else:
            return False
