# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array Given an array nums of n integers where
# nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

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
