class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        inc = [0]*n
        dec = [0]*n 


        for i in range(n):
            for j in range(i+1):
                if rating[i] < rating[j]:
                    dec[i] += 1
                elif rating[i] > rating[j]:
                    inc[i] += 1
        
        ans = 0

        for i in range(n-1,-1,-1):
            for j in range(i-1,-1,-1):
                if rating[i] < rating[j]:
                    if dec[j] > 0:
                        ans += dec[j]
                if rating[i] > rating[j]:
                    if inc[j] > 0:
                        ans += inc[j]
        
        return ans