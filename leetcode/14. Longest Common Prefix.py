from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs, key=len)
        strs.remove(min_str)
        result = ''

        for char in min_str:
            pref = result + char
            for s in strs:
                if not s.startswith(pref):
                    return result
            result += char

        return result
