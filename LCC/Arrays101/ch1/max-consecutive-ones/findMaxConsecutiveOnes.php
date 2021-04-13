/*
* https://leetcode.com/problems/max-consecutive-ones
* Given a binary array, find the maximum number of consecutive 1s in this array.
*
* Time complexity: O(n)
* Runtime: 120ms
* Memory: 16mo
*/

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaxConsecutiveOnes($nums) {
        $maxConsecutive = 0;
        $currentMax = 0;

        forEach($nums as $num){
          if($num == 0) {
            $currentMax = 0;
            continue;
          }
          $currentMax++;
          if($currentMax > $maxConsecutive) {
            $maxConsecutive = $currentMax;
          }
        }

        return $maxConsecutive;
    }
}