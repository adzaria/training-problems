/**
 * https://leetcode.com/problems/two-sum-iii-data-structure-design/
 * Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.
 *
 * Personal notes: This is a very straightforward and pretty bad implementation considering time and space complexities. Writing this just allowed me to write a working 'solution' in just 10 seconds...
 * Adding a number is slow because we are storing a set for all possible sums on each add.
 * Finding is O(n) at worse for n stored values.
 * Improvements: the stored values should be sorted to allow either two-pointers-search or O(log(n)) search
 *
 * Runtime: 7480ms (faster than 7%)
 * Memory: 50mb (less than 69%)
 */
class TwoSum {
  
  private values: number[];
  private allSums: any = new Set();
  
  constructor() {
    this.values = [];
  }
  
  add(number: number): void {
    for(let value of this.values) {
      this.allSums.add(value + number);
    }
    this.values.push(number);
  }
  
  find(value: number): boolean {
    return this.allSums.has(value);
  }
}
