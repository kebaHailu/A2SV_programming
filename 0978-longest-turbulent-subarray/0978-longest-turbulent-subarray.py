class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        left = 0
        right = 0
        max_len = 0 

        if len(arr) < 2 :
            return 1


        while right < len(arr):

            
            while right < len(arr)-1 and (arr[right-1] > arr[right] < arr[right+1] or arr[right-1] < arr[right] > arr[right+1]) :
                right += 1 

           

            while left < right and arr[left] == arr[left + 1]:
                left += 1 

            max_len = max(max_len,right-left+1)
            left = right
            right +=1

        return max_len 
    