class Solution:
    def simplifyPath(self, path: str) -> str:

        s_path = path.split("/")
        

        stack = []
        for s in s_path:
            if s == '':
                continue

            elif s == '..' :
                if stack:
                    stack.pop()
                continue  
            elif s == '.':
                continue 
            else:
                stack.append(s) 

        newstack = '/' + '/'.join(stack)
        return (newstack)

                
            