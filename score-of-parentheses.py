class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        return self.ans(s,0,len(s)-1)
    

    def ans(self,s_in,left,right):

        if right - left == 1:
            return 1 

        
        count = 0 

        for idx in range(left,right):
            if s_in[idx] == '(':
                count += 1
            elif s_in[idx] == ')':
                count -= 1 
            if count == 0:
                return self.ans(s_in,left,idx) + self.ans(s_in,idx+1,right)
            
        return 2 * self.ans(s_in,left+1,right-1)