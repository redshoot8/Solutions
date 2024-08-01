class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        elif numRows == 2:
            new_string = ''
            for i in range(0, len(s), 2):
                new_string += s[i]
            for i in range(1, len(s), 2):
                new_string += s[i]
            return new_string

        array = [[]]
        counter = 0
        down = True
        index = numRows - 2
        while counter < len(s):
            if down:
                array[-1].append(s[counter])
                if len(array[-1]) % numRows == 0:
                    down = False
                    array.append([])
            else:
                array[-1] = ['' if i != index else s[counter] for i in range(numRows)]
                array.append([])
                if index == 1:
                    down = True
                    index = numRows - 2
                else:
                    index -= 1
            counter += 1
            
        while len(array[-1]) < numRows:
            array[-1].append('')
        
        new_string = ''
        for i in range(numRows):
            for j in range(len(array)):
                new_string += array[j][i]
        
        return new_string
