/**
* https://leetcode.com/problems/merge-sorted-array
* Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
* The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
*
* Time complexity: O(n)
* Tests runtime: 160ms (faster than 56%)
* Tests memory: 35mo (less than 75%)
*/

class Solution {
    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
      var _m = m-1;
      var _n = n-1;
      for(j in (m + n - 1) downTo 0) {
          if((_m >= 0) and (_n >= 0)) {
            if(nums1[_m] > nums2[_n]){
               nums1[j]=nums1[_m];
               _m--;
            } else {
              nums1[j]=nums2[_n];
              _n--;
            }
          } else {
            if(_n >= 0){
              nums1[j]=nums2[_n];
              _n--;
            } else if (_m >= 0) {
              nums1[j]=nums1[_m];
              _m--;
            }
          }
      }
    }
}