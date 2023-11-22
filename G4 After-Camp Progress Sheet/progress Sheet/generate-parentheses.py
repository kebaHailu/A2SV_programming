class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

    
        poss = ['(']*(n*2)
        
        
        
        ans = list() 

        def valid(arr):
            if arr.count('(') != arr.count(')'): return False
            stack = []
            while arr:
                cur = arr.pop() 
                if cur == ')':
                    stack.append('(')
                else:
                    if not stack:return False
                    stack.pop() 
            return not stack
        
        
        def dp(idx,parss):
            if idx >= len(parss) :
                if valid(parss.copy()):
                    ans.append(''.join(parss))
                return 
            
            
            
            dp(idx+1,parss.copy())
         
            parss[idx] = ")"
            dp(idx+1,parss.copy())
        
        dp(0,poss)

        return ans
        
