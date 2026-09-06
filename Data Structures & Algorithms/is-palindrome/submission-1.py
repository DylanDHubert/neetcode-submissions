import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_altered = s.lower()
        L, R = 0, len(s) - 1
        while L < R:
            if not s_altered[L].isalnum():
                L += 1
                continue
            if not s_altered[R].isalnum():
                R -= 1
                continue
            if s_altered[L] != s_altered[R]:
                return False
            L += 1
            R -= 1
        return True
        