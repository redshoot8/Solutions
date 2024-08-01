class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ''    
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                if self.isPalindrome(s[i:j]) and len(s[i:j]) > len(max_palindrome):
                    max_palindrome = s[i:j]
        return max_palindrome
    
    def isPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        return False
