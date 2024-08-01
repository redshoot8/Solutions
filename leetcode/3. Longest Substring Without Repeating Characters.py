class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        cur_vocab = []
        for char in s:
            if char in cur_vocab:
                max_length = max(max_length, len(cur_vocab))
                cur_vocab = cur_vocab[cur_vocab.index(char) + 1:]
            cur_vocab.append(char)
        max_length = max(max_length, len(cur_vocab))
        return max_length
