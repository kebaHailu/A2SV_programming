class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left < 2 and right > 2:
            return [2,3]
        def is_prime(n):
            d = 2

            while d*d <= n:
                if n%d == 0:
                    return False 
                d += 1 
            return True 

        stack = []
        min_prime = [-1,-1]
        

        for i in range(left,right+1):
            if is_prime(i):
                stack.append(i)
            if len(stack)>1 and stack[-1]-stack[-2] <= 2:
                return [stack[-2],stack[-1]]

        min_val = float("inf")    
        for i in range(1,len(stack)):
            if stack[i]-stack[i-1] < min_val:
                min_val = stack[i] - stack[i-1]
                min_prime = [stack[i-1],stack[i]]
              

        
        return min_prime