/**
* https://leetcode.com/problems/duplicate-zeros
* Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
* Note that elements beyond the length of the original array are not written.
* Do the above modifications to the input array in place, do not return anything from your function.
*
* Time complexity:
* Tests runtime: ms (faster than %)
* Tests memory: mo (less than %)
*/
class Solution {
    fun duplicateZeros(arr: IntArray): Unit {

      for(j in arr.size - 1 downTo 0) {

        if(arr[j]===0) {

          for (i in (arr.size - 1) downTo j + 1) {
            arr[i] = arr[i-1];
          }
        }
      }
    }
}