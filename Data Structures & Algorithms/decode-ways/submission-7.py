class Solution:
    def numDecodings(self, s: str) -> int:
        def check(n):
            if n[0] == "0": return False
            shifted = int(n)
            if (0 < shifted < 27): return True
            return False

        if not check (s[0]): return 0  

        solution = 1

        # NEED TO GO IN REVERSE, SINCE WAYS s[i] DEPENDS ON WAYS s[i+1] & (IF [i:i+2] VALID) s[i+2]
        # NEITHER VALID, DEAD END... 0s ALL THE WAY DOWN...

        curr, prev, prev_prev = 0, 1, 0

        print("c p pp i i:")

        i = len(s) - 1
        while i > -1:
            if (i+1<len(s)) and (s[i] == s[i+1] == 0): return 0  # "00" BREAKS DECODING

            curr = 0

            if check(s[i]): curr += prev # WE CAN DECODE THIS ONE, 

            if (i+1<len(s)) and check(s[i:i+2]): 
                print("!")
                curr += prev_prev
            
            print(curr, prev, prev_prev, s[i], s[i:i+2])

            prev_prev = prev
            prev = curr

            i -= 1
       
        return curr


