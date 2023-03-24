class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k 
        cur_unfair = float("inf")
 


        def backtrack(cookies,idx):
            nonlocal cur_unfair
            if idx == len(cookies):
                
                cur_unfair = min(cur_unfair,max(child))

                return 
            if cur_unfair < max(child):
                return 

            for i in range(len(child)):

                child[i] += cookies[idx]
                backtrack(cookies,idx+1)
                child[i] -= cookies[idx]

            
        backtrack(sorted(cookies,reverse=True),0)
        return cur_unfair