class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        def dfs(idx,check):
            if idx == len(requests):
                return 0 if all(b==0 for b in check) else float("-inf")
            lst = list(check)
            lst[requests[idx][1]] += 1
            lst[requests[idx][0]] -= 1 
            return max(dfs(idx+1, tuple(lst))+1, dfs(idx+1,check)) 

        bls = tuple([0]*n)
        return dfs(0,bls)