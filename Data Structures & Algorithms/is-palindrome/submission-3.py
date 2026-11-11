import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([c for c in s if c.isalnum()])
        
        IDX = 0
        
        while IDX < (len(s) // 2):
            RDX = -(IDX+1)
            if s[IDX] != s[RDX]: return False

            IDX += 1
        
        return True
        
        
