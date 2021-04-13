# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/ Given an array arr,
# replace every element in that array with the greatest element among the elements to its right, and replace the last
# element with -1. After doing so, return the array.
#
# Personal note: answer was straight forward, it could probably be simplified to be easier to use, but time and space
# complexity are good
#
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def replaceElements(self, arr):
        biggest_number = -1
        for i in range(len(arr) - 1, -1, -1):
            biggest_number_temp = -1
            if arr[i] > biggest_number:
                biggest_number_temp = arr[i]
            arr[i] = biggest_number
            if biggest_number_temp > biggest_number:
                biggest_number = biggest_number_temp

        return arr
