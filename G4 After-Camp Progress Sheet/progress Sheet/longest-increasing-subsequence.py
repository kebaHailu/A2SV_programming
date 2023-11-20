class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        stack = [inf]

        for n in nums:
            i = bisect_left(stack,n)
            if len(stack) == i:
                stack.append(n)
            else:
                stack[i] = n 
        
        return len(stack)