/**
 * https://leetcode.com/problems/two-sum/
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 *
 * Personal note: seems pretty bad as each element of an array of length n will be checked n times, which is O(n²)
 *
 * Runtime: 88ms (faster than 34%)
 * Memory: 39.2mo (less than 96%)
 */
function twoSum(nums: number[], target: number): number[] {
  for(let indexOfTestedNumber = 0; indexOfTestedNumber < nums.length; indexOfTestedNumber++) {
    for(let indexOfTestedNumber2 = 0; indexOfTestedNumber2 < nums.length; indexOfTestedNumber2++) {
      if(indexOfTestedNumber === indexOfTestedNumber2) continue;
      if(nums[indexOfTestedNumber] + nums[indexOfTestedNumber2] === target) {
        return [indexOfTestedNumber, indexOfTestedNumber2];
      }
    }
  }
  return [];
}