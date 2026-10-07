class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer = 0
        for c in s:
            if pointer == len(t):
                break
            if c == t[pointer]:
                pointer += 1
        return len(t) - pointer