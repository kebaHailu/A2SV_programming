class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def reverse(x):
            return x[::-1]

        def invert(x):
            s = ""
            for i in x:
                if i == "0":
                    s += "1"
                else :
                    s += "0"
            return s 
                    
        def bs(n):
            
            if n == 1:
                return "0"
            
            return bs(n-1) + "1" + reverse(invert(bs(n-1)))

        return bs(n)[k-1]