# Letter Combinations of a Phone Number

class Solution(object):
    def letterCombinations(self, digits):

        if digits == "" :
            return []

        mapping = {
             '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = ['']
        
        for d in digits:
            new_list = []

            for comb in result:
                for letter in mapping[d]:
                    new_list.append(comb + letter)

            result = new_list

        return result
