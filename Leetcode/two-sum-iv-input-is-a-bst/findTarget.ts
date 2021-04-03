/**
 * https://leetcode.com/problems/two-sum-iv-input-is-a-bst/submissions/
 * Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
 *
 * Personal note: This solution iterates once on each item of the tree using recursion (O(n)).
 *
 * Runtime: 116ms (faster than 86%)
 * Memory: 47mo (less than 89%)
 */
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
  }
}

function findTarget(root: TreeNode | null, k: number): any {
  const remainders: any = new Set();
  
  function inspectTree(fromRoot: TreeNode | null) {
    if(remainders.has(fromRoot?.val)) return true;
    if(remainders.has(fromRoot?.left?.val)) return true;
    if(remainders.has(fromRoot?.right?.val)) return true;
    remainders.add(k - (fromRoot?.val));
    if(fromRoot?.left && inspectTree((fromRoot).left)) return true;
    if(fromRoot?.right && inspectTree((fromRoot).right)) return true;
  }
  
  return inspectTree(root) ?? false;
}