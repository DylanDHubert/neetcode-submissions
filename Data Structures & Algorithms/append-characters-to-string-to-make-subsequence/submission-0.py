class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        exists = ""
        pointer = 0
        for c in s:
            if pointer == len(t):
                break
            if c == t[pointer]:
                exists += c
                pointer += 1
        return len(t) - len(exists) 