class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7 
        tot = 0
        arr.append(0)
        stack = [-1]
        for i , num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                index = stack.pop()
                first = stack[-1]
                left = index - first
                right = i - index
                tot += right * left * arr[index]
            stack.append(i)
        return tot%mod