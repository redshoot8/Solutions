class Solution:
    roman_vocabulary = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    def intToRoman(self, num: int) -> str:
        roman_num = ''

        for roman, integer in Solution.roman_vocabulary.items():
            while num - integer >= 0:
                num -= integer
                roman_num += roman

        return roman_num
