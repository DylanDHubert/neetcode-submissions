class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}
        
        def c(target, pointer):
            key = str(target) + "+" + str(pointer)

            if target == 0: return 1
            if target < 0: return 0

            if memo.get(key) is not None: return memo[key]
            
            result = 0

            for index, denom in enumerate(coins):
                if index < pointer: continue
                result += c(target-denom, index)
            
            memo[key] = result
            return result
        
        return c(amount, 0)