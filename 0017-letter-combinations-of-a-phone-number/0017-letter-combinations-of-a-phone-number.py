class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(index:int, letter:str):
            if len(letter) == len(digits):
                results.append(letter)
                return
            
            for i in range(index, len(digits)):
                for j in number_letter_map[digits[i]]:
                    dfs(i+1, letter + j)
        
        number_letter_map= {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        if len(digits) == 0:
            return []
        
        results = []
        
        dfs(0, "")
        
        return results
        

        