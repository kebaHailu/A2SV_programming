class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = Counter()
        for i in bills:
            count[i] += 1
            if i == 10:
                if count.get(5,0):
                    count[5] -= 1
                else:
                    return False 
            elif i == 20:
                if (count.get(5,0) and count.get(10,0)):
                    count[5] -= 1
                    count[10] -= 1
                
                elif (count.get(5,0) and count[5] > 2):
                    count[5] -= 3
                else:
                    return False 
        
        return True