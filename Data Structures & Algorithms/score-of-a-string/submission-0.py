class Solution:
    def scoreOfString(self, s: str) -> int:
        ordinals = [ord(c) for c in s]
        scores = [abs(ordinals[i+1] - ordinals[i]) for i in range(len(s)-1)]
        return sum(scores)
