class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        n = len(word1)
        k = len(word2)
        for i in range(min(n, k)):
            res += word1[i]
            res += word2[i]
        if len(word1) >= len(word2):
            res += word1[len(word2):]
        elif len(word1) < len(word2):
            res += word2[len(word1):]
        return res


        