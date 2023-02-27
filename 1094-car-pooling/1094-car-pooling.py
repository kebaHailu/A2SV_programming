class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        inital = []
        final = []
        
        for trip in trips:
            numpass , from_ , to_ = trip 
            if to_ < from_ :
                return False 
            inital.append(from_)
            final.append(to_)
            
        inital.sort()
        final.sort()
       
        
        length = final[-1] - inital[0] + 1
        alltrip = [0] * (length)
        
        for trip in trips:
            numpass , from_ , to_ = trip 
            
            alltrip[from_-inital[0]] += numpass
            alltrip[to_ -inital[0]] -= numpass 
            
        for i in range(1,len(alltrip)):
            alltrip[i] += alltrip[i-1]
        
        
        return max(alltrip) <= capacity
       
    