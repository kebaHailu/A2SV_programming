class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        i = 0
        prev = max(arr)
        while i < len(arr)-1:
            if arr[i] < prev:
                arr[i] = prev
            else:
                
                prev = max(arr[i+1:])
                arr[i] = prev
            i += 1
        arr[-1] =-1
        return arr