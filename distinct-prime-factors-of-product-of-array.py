class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

         # we don't have to product the array, instead we just need prime numbers for 
        # every element which is equal to the final product prime numbers 
        
        
        # first I write a function that can calculate prime factorization
        def pf(n):
            factors = set()
            d = 2 
            
            while d*d <= n:
                while n%d == 0:
                    factors.add(d)
                    n //= d 
                
                d += 1 
            
            if n > 1:
                factors.add(n)
            return factors 
        # then for every element we will add if there is a new prime number to ans
        ans = set()
        for i in nums:
            ans |= pf(i) # for every element we will see if there is a new prime number 
            # and if we find new prime number we will add to our set 
        
        
        
        return len(ans)