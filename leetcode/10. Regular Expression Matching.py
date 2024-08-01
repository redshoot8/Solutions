class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        if len(s) == 0:
            return len(p) > 1 and p[1] == '*' and self.isMatch(s, p[2:])
        
        if len(p) > 1 and p[1] == '*':
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
        else:
            return (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
