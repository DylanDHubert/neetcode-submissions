class Solution:
    def numDecodings(self, s: str) -> int:

        def check(num):
            num = int(num)
            if (0 < num < 27): return True
            return False

        memo = {}
        
        def rDecode(pointer=0):
            if memo.get(pointer) is not None: return memo[pointer]

            # BASE CASE (OOB), INVALID
            if pointer >= len(s): return 1 # END OF STRING, NO NEW WAY FOUND


            solution = 0
            if check(s[pointer]):
                solution += rDecode(pointer+1)
            else: 
                memo[pointer] = solution
                return solution
            if check(s[pointer:pointer+2]) and (pointer + 1 < len(s)):
                solution += rDecode(pointer+2)
            
            memo[pointer] = solution
            return solution
        
        return rDecode()