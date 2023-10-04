class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        @cache 
        def dp(idx):
            if idx == len(s):
                return 1 
            
            if int(s[idx]) == 0:
                return 0 
            
            val = dp(idx+1)

            if idx+1 < len(s) and int(s[idx]+s[idx+1]) < 27:
                val += dp(idx+2)
            
            return val
        

        return dp(0)