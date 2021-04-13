# https://leetcode.com/problems/sort-array-by-parity Given an array A of non-negative integers, return an array
# consisting of all the even elements of A, followed by all the odd elements of A. You may return any answer array
# that satisfies this condition.
#
# Personal note: solution is very straightforward but time and space complexity are very good
#
# Time complexity: O(n)
# Space complexity: O(1)
# Tests runtime: 76ms (faster than 82%)
# Tests memory: 15mo (less than 25%)

class Solution:
    def sortArrayByParity(self, A):
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] % 2 == 0:
                i += 1
                continue
            if A[j] % 2 == 1:
                j -= 1
                continue
            buffer = A[i]
            A[i] = A[j]
            A[j] = buffer
            i += 1
            j -= 1
        return A
