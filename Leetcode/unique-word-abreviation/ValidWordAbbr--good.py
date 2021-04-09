# https://leetcode.com/problems/unique-word-abbreviation/ The abbreviation of a word is a concatenation of its first
# letter, the number of characters between the first and last letter, and its last letter. If a word has only two
# characters, then it is an abbreviation of itself. Implement the ValidWordAbbr class: ValidWordAbbr(String[]
# dictionary) Initializes the object with a dictionary of words. boolean isUnique(string word) Returns true if either
# of the following conditions are met (otherwise returns false): There is no word in dictionary whose abbreviation is
# equal to word's abbreviation. For any word in dictionary whose abbreviation is equal to word's abbreviation,
# that word and word are the same.
#
# Runtime: 208ms (faster than 84%)
# Memory: 24mb (less than 94%)

class ValidWordAbbr:
    def __init__(self, dictionary):
        self.__dictionary = {}
        for word in dictionary:
            abbreviation = self.__getAbbreviation(word)
            if abbreviation not in self.__dictionary:
                self.__dictionary.update({abbreviation: word})
            elif self.__dictionary[abbreviation] != word:
                self.__dictionary.update({abbreviation: False})

    def __getAbbreviation(self, word):
      if len(word) > 2:
        return word[0] + str((len(word) - 2)) + word[len(word) - 1]
      return word

    def isUnique(self, word):
        abbreviation = self.__getAbbreviation(word)
        if abbreviation not in self.__dictionary or self.__dictionary[abbreviation] == word:
            return True
        return False
