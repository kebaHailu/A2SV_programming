class Solution:
    def numTrees(self, n: int) -> int:
        
        lookup = {} # int:int 

        def dp(n):
            if n == 1:
                return 1 

            ans = 0
            for i in range(1,n+1):
                x = 1 if i-1 ==0 else i-1
                y = 1 if n-i == 0 else n-i

                if x in lookup:
                    val_x = lookup[x]
                else: val_x = dp(x)
                if y in lookup:
                    val_y = lookup[y]
                else: val_y = dp(y) 
                ans += val_x * val_y
            
            lookup[n] = ans 
            return ans
        
        return dp(n)