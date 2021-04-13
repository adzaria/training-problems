# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the
# new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place
# with O(1) extra memory.
#
# Time complexity O()
# Space complexity O()

class Solution:
    def removeDuplicates(self, nums):
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        return i
