class Solution:
    def countPrimes(self, n: int) -> int:
        def sieve(n):
            if n < 3: return 0
           
            prime_count = 0
            is_prime = [True]*(n+1)
            is_prime[0] = is_prime[1] = False 

            for i in range(2,int(sqrt(n))+1):
                if is_prime[i]:
                    for j in range(i*i,n+1,i):
                        is_prime[j] = False 
            is_prime.pop()
            for is_sure in is_prime:
                if is_sure:
                    prime_count += 1
           
            return prime_count 
        
        return sieve(n)