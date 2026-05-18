class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phones = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        def back(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                num = digits[index]
                for letter in phones[num]:
                    combination.append(letter)
                    back(index + 1)
                    combination.pop()
        
        combination = []
        combinations = []

        back(0)
        return combinations
        