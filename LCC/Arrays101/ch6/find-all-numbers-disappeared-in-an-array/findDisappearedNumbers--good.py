# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array Given an array nums of n integers where
# nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
#
# Personal note: although time complexity is O(n) (and the set could be a hashmap), the space is O(n), and the
# question says there is a O(1) solution
#
# Time complexity: O(n)
# Space  complexity: O(1)

class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        s = set()
        for i in range(n):
            s.add(i + 1)
        for num in nums:
            if num in s:
                s.remove(num)

        return list(s)
