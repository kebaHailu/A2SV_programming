class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        max_index = arr.index(max(arr))
        if max_index != 0 and max_index != len(arr)-1:
            
        
            
            cond2 = all(arr[i] < arr[i+1] for i in range(max_index))
            cond3 = all(arr[i] > arr[i+1] for i in range(max_index,len(arr)-1))
            

            if (cond2 and cond3) :
                return True
        return False
    
            
                