class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        if n&1:
            flag = False

            while n:
                if n&1 and not flag:
                    flag = True 
                elif not n&1 and flag:
                    flag = False
                else:
                    return False
                n >>= 1
        else:
            flag = True 
            while n:
                if n&1 and not flag:
                    flag = True 
                elif not n&1 and flag:
                    flag = False 
                else:
                    return False
                n >>= 1
            
        return True