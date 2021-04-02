/**
 * Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
 * Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
 * You may assume that each input would have exactly one solution and you may not use the same element twice.
 *
 * Personal note: this brute-force solution uses maps, so it is O(n) but it does not use the sorted quality of the array
 *
 * Runtime: 76ms (faster than 97%)
 * Memory: 40.1mo (less than 20%)
 */

function twoSum(nums: number[], target: number): number[] {
  const numsMap: any = {};
  for(let indexOfTestedNumber = 0; indexOfTestedNumber < nums.length; indexOfTestedNumber++) {
    const currentNumber = nums[indexOfTestedNumber];
    const quantityLeft = target - currentNumber;
    if(typeof numsMap[currentNumber] !== "undefined") {
      if(indexOfTestedNumber < numsMap[currentNumber]) {
        return ([indexOfTestedNumber + 1, numsMap[currentNumber]+1]);
      }
      return ([numsMap[currentNumber]+1, indexOfTestedNumber + 1]);
    }
    numsMap[quantityLeft] = indexOfTestedNumber;
  }
}