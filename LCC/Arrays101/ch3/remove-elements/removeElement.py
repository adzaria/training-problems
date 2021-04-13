# https://leetcode.com/problems/remove-element/solution/
#
# Given an array nums and a value val, remove all instances of that value in-place and return the new length. Do not
# allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra
# memory. The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeElement(self, nums, val: int):
        i = 0
        original_length = len(nums)
        for j in range(original_length):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
