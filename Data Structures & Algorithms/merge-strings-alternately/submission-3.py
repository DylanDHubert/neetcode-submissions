class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        solution = ""
        I = 0
        while True:
            if I == len(word1):
                solution += word2[I:]
                break
            if I == len(word2):
                solution += word1[I:]
                break
            solution += word1[I]
            solution += word2[I]
            I += 1
        return solution