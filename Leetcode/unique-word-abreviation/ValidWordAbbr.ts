/**
 * https://leetcode.com/problems/unique-word-abbreviation/
 * The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last letter, and its last letter. If a word has only two characters, then it is an abbreviation of itself.
 * Implement the ValidWordAbbr class:
 *    ValidWordAbbr(String[] dictionary) Initializes the object with a dictionary of words.
 *    boolean isUnique(string word) Returns true if either of the following conditions are met (otherwise returns false):
 *    There is no word in dictionary whose abbreviation is equal to word's abbreviation.
 *    For any word in dictionary whose abbreviation is equal to word's abbreviation, that word and word are the same.
 *
 * Personal note:
 * In the end it is just a basic hashtable implementation.
 * Initialization could be improved, I used the Set to solve it faster
 * isUnique is a pretty straightforward implementation of the problem that is O(1) time complexity.
 *
 * Runtime: 196ms (faster than 100%)
 * Memory: 57mo (less than 100%)
 */
class ValidWordAbbr {
  
  private dictionaryMap: {
    [key: string]: string[]
  } = {}; // abr => [words]
  
  constructor(dictionary: string[]) {
    for(let word of dictionary) {
      const wordAbbreviation = this.getAbbreviation(word);
      this.dictionaryMap[wordAbbreviation] = [
        ...new Set([...(this.dictionaryMap[wordAbbreviation] ?? []), word])];
    }
  }
  
  private getAbbreviation(word: string): string {
    const wordLength = word.length;
    if (wordLength === 1) return word;
    return `${word[0]}${wordLength > 2 ? wordLength - 2 : ""}${word[wordLength - 1]}`;
  }
  
  public isUnique(word: string): boolean {
    const wordAbbreviation = this.getAbbreviation(word);
    const doesAbbreviationExist = !!this.dictionaryMap[wordAbbreviation];
    const words = this.dictionaryMap[wordAbbreviation];
    if(!doesAbbreviationExist) return true;
    if(doesAbbreviationExist) {
      if(words.length === 1 && words[0] === word) return true;
    }
    return false;
  }
}
