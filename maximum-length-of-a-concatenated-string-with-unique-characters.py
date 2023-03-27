class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0 

        def backtrack(idx,strs):
            nonlocal max_len
            if len(strs) != len(set(strs)):
                return 
            
            max_len = max(max_len,len(strs))

            for i in range(idx,len(arr)):
                backtrack(i+1,strs+arr[i])

        backtrack(0,"")
        return max_len