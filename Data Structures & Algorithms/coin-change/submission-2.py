class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def change(total=0):
            if total == amount: return 0
            if memo.get(total) is not None: return memo[total]
            
            result = 1e6
            for c in coins:
                if total + c > amount:
                    continue
                result = min(result, 1 + change(total + c))
            
            memo[total] = result
            return result
        
        result = change()
        return result if result < 1e6 else -1
        
