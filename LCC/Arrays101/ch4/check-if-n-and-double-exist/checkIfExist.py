# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/ Given an array
# arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M). More
# formally check if there exists two indices i and j such that :
# i != j 0 <= i,
# j < arr.length
# arr[i] == 2 * arr[j]

class Solution:
    def checkIfExist(self, arr):
        map_numbers = {}
        for num in arr:
            if 2 * num in map_numbers:
                return True
            if num % 2 == 0 and num / 2 in map_numbers:
                return True
            map_numbers[num] = True
        return False
