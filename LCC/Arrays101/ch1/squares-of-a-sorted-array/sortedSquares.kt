/**
* https://leetcode.com/problems/squares-of-a-sorted-array/ Given an integer array nums sorted
* in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
*
* Time complexity: O(n)
* Tests runtime: 204ms
* Tests memory: 16mo
*/

class Solution {
    fun sortedSquares(nums: IntArray): IntArray {
        var i = 0;
        var j = nums.size - 1

        val squares = Array(nums.size, {i-> 0})

        for(n in nums.size - 1 downTo 0) {
          val squareI = nums[i] * nums[i];
          val squareJ = nums[j] * nums[j];

          if(squareI < squareJ) {
            squares[n] = squareJ;
            j--;
          } else {
            squares[n] = squareI;
            i++
          }
        }

        return squares.toIntArray();
    }
}