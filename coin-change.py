class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(n):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
           
            
            s = float("inf")
            for i in range(len(coins)):
              
                val = n - coins[i]
                
                if val >= 0:
                    s = min(s,dp(val))

            memo[n] = s + 1
            return memo[n]

        x = dp(amount)
        return x if x != float("inf") else -1