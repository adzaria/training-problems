/*
* https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
* Given a binary array, find the maximum number of consecutive 1s in this array.
*
* Runtime: 72ms (faster than 99%)
* Memory: 40mo (less than 20%)
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