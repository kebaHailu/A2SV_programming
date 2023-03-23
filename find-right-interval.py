class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
       # the array will put every start value sorted with there primery index so it will be ready for binary search when we find the element we will return the index of that element 
        arr = [[i[0],intervals.index(i)] for i in sorted(intervals,key=lambda x:x[0])]
        
        # this function will return the searched element's index or -1 if the next element does not exits 
        def f(k):

            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = left + (right - left )//2
                
                if k == arr[mid][0]:
                    return arr[mid][1]

                elif k < arr[mid][0]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # if the the left index is not out of the range then we will return the next left index except -1 will be returned 
            try :
                return arr[left][1]
            
            except:

                return -1
        ans = []
        for j,i in intervals:
            ans.append(f(i))


        
        return ans