class Solution:
    def romanToInt(self, s: str) -> int:
        sorted_roman_vocabulary = {
            'CM': 900,
            'CD': 400,
            'XC': 90,
            'XL': 40,
            'IX': 9,
            'IV': 4,
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        integer_num = 0

        for roman, integer in sorted_roman_vocabulary.items():
            integer_num += integer * s.count(roman)
            s = s.replace(roman, '_')

        return integer_num
