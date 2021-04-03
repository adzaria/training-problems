/**
 * https://leetcode.com/problems/two-sum/
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 *
 * Personal note: this one should only be O(n)
 *
 * Runtime: 80ms (faster than 96%)
 * Memory: 39.2mo (less than 99%)
 */
function twoSum(nums: number[], target: number): number[] {
  const numsMap: any = {};
  for(let indexOfTestedNumber = 0; indexOfTestedNumber < nums.length; indexOfTestedNumber++) {
    const currentNumber = nums[indexOfTestedNumber];
    const quantityLeft = target - currentNumber;
    if(typeof numsMap[currentNumber] !== "undefined") return ([indexOfTestedNumber, numsMap[currentNumber]]);
    numsMap[quantityLeft] = indexOfTestedNumber;
  }
  return [];
}