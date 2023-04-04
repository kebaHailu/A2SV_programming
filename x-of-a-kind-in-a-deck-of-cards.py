class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)

        
        arr = list(map(int,count.values()))
        hcf = arr[0]
        
        for i in range(1,len(arr)):
            hcf =gcd(hcf,arr[i])
        

        if hcf > 1:
            return True 
        
        return False