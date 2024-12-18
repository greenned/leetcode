class Solution:
    def isValid(self, s: str) -> bool:
        

        bracket_map = {"(":")", "{":"}", "[":"]"}
        open_brackets = bracket_map.keys()
        close_brackets = bracket_map.values()

        stack = []
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                
                if len(stack) ==0:
                    return False

                last_bracket = stack.pop(-1)
                if bracket_map[last_bracket] != bracket:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                
