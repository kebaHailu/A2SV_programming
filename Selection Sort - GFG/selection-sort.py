#User function Template for python3

class Solution: 
    def select(self, arr, i,n):
        # code here 
        my_min = arr[i]
        min_idx = i
        while i < n:
            if arr[i] < my_min:
                my_min = arr[i]
                min_idx = i
            i += 1
        return min_idx
        
        
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            slct = self.select(arr,i,n)
            arr[i],arr[slct] = arr[slct],arr[i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends