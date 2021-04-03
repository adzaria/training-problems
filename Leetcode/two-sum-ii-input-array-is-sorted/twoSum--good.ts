/**
 * https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/
 * Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
 * Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
 * You may assume that each input would have exactly one solution and you may not use the same element twice.
 *
 * Personal note: This solution also is O(n) (see two-code), but it uses the 'sorted' property of the input
 *
 * Runtime: 72ms (faster than 99%)
 * Memory: 40mo (less than 20%)
 */

function twoSum(nums: number[], target: number): number[] {
  let i = 0;
  let j = nums.length - 1;
  while(j > i) {
    const sum = nums[i] + nums[j];
    if(sum === target) return[i + 1, j + 1];
    if(sum < target) {
      i++;
    } else {
      j--;
    }
  }
}