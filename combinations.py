class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combination = []

        def backtrack(idx,path):
            if len(path) == k:
                combination.append(path[:])
                return

            for i in range(idx,n+1):
                path.append(i)
                backtrack(i+1,path)
                path.pop()

        
        backtrack(1,[])
        return combination