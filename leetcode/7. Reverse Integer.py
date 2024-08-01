class Solution:
    def reverse(self, x: int) -> int:
        sign = ''
        if x < 0:
            sign = '-'
        x = str(abs(x))[::-1]
        if int(x) > 2 ** 31 - 1:
            return 0
        return int(sign + x)