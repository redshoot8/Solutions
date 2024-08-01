class Solution:
    def myAtoi(self, s: str) -> int:
        new_string = ''
        without_spaces = s.strip()
        
        for i in range(len(without_spaces)):
            if i == 0 and without_spaces[i] in '+-':
                new_string += without_spaces[i]
            elif without_spaces[i].isdigit():
                new_string += without_spaces[i]
            else:
                break
        
        if new_string in ' +-':
            return 0
        
        integer = int(new_string)
        
        if integer > 2**31 - 1:
            return 2**31 - 1
        elif integer < -2**31:
            return -2**31
        return int(new_string)
