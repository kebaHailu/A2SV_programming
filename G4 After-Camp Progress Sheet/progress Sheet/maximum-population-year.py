class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        store = Counter() 

        for start , end in logs:
            for i in range(start,end):
                store[i] += 1 
        

        max_val = year = 0
        for key , val in store.items():
            if val > max_val:
                max_val = val 
                year = key
            if val == max_val:
                year = min(year,key) 
        return year
