class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                
                c = a + b
                stack.append(c)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                
                c = b - a
                stack.append(c)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                
                c = a * b
                stack.append(c)
            
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                
                c = int(b / a)
                stack.append(c)
            else :
                stack.append(int(token))
            
        return stack[0]
            
                
            