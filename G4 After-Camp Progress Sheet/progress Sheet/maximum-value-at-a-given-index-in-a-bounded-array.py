class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sumfun(idx,end):
            if idx == 0:
                return 0
            start = max(end-idx,0)
            sum1 = end * ( end+1)//2 
            sum2 = start * ( 1 + start)//2 
            return sum1 - sum2 
        

        maxSum -= n
        left , right = 0,maxSum 
        while left <= right:
            mid = (left + right)//2 
            left_sum = sumfun(index+1,mid)
            right_sum = sumfun(n-index-1,mid-1)
            if left_sum + right_sum <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
        
        return left 
