class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        i = 0 
        j = 50000

        while j > i:
            if i * i + j * j == c: 
                return True 


            elif i * i + j * j > c:
                j -= 1 
            elif i * i + j * j < c:
                i += 1 
        if i * i + j*j == c:
            return True
        return False
