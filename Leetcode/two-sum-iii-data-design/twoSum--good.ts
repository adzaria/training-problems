/**
 * https://leetcode.com/problems/two-sum-iii-data-structure-design/
 * Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.
 *
 * Personal notes:
 * Add operation takes O(n). The values are sorted.
 * Find operation also is O(n). It uses 2 pointers to iterate on the list.
 * Improvements:
 * We could use a better strategy to make the add operation O(log(n)) for time
 *
 * Runtime: 256ms (faster than 77%)
 * Memory: 47mb (less than 100%)
 */
class TwoSum {
  
  private values: number[];
  
  constructor() {
    
    this.values = [];
  }
  
  add(number: number): void {
    
    if(this.values.length === 0) {
      this.values.push(number);
      return;
    }
    
    if(number <= this.values[0]) {
      this.values.unshift(number);
    }
    
    for(let j = (this.values.length - 1); j >= 0; j--) {
      if(number > this.values[j]) {
        this.values.splice(j + 1, 0, number);
        break;
      }
    }
  }
  
  find(value: number): boolean {

    let i = 0;
    let j = this.values.length - 1;

    while(i < j) {
      if(this.values[i] + this.values[j] === value) {
        return true;
      }
      if(this.values[i] + this.values[j] < value) {
        i++;
      } else {
        j--;
      }
    }
    
    return false;
  }
}
