# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/ A school is trying to take an annual
# photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height.
# Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith
# student in line. You are given an integer array heights representing the current order that the students are
# standing in. Each heights[i] is the height of the ith student in line (0-indexed). Return the number of indices
# where heights[i] != expected[i].
#
# Time complexity: limited by the sorted() function
# Space complexity: O(n)
# Tests runtime: ms (faster than %)
# Tests memory: mo (less than %)

class Solution:
    def heightChecker(self, heights):
        counter = 0
        duplicated_heights = sorted(self.duplicate(heights))
        for i in range(len(heights)):
            if heights[i] != duplicated_heights[i]:
                counter += 1
        return counter

    def duplicate(self, arr):
        arr2 = [0] * len(arr)
        for i in range(len(arr)):
            arr2[i] = arr[i]
        return arr2
