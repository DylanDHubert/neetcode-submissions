class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * n

        def climb(pos=0):
            if pos > n: return 0 
            if pos == n: return 1
            if memo[pos] is not None: return memo[pos]

            # TRY ONE STEP, TRY TWO
            result = climb(pos + 1) + climb(pos + 2)
            memo[pos] = result
            return result

        return climb()
