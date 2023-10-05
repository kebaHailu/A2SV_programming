class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        lookup = {}
        def dfs(n,idx):
            if n == len(triangle) :
                return 0
            
            if (n,idx) in lookup:
                return lookup[(n,idx)]
            
            ans = triangle[n][idx] 
            ans += min(dfs(n+1,idx) , dfs(n+1,idx+1))
            lookup[(n,idx)] = ans
            return ans
            
        
        val = dfs(0,0)

        return val