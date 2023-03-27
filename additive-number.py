class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        cur = []

        def backtrack(idx):
            if idx == len(num):
                print(cur)
                return len(cur) >= 3
                
            
            for i in range(idx+1,len(num)+1):
                
                if num[idx] != '0' or len(num[idx:i]) == 1:
                    n = int(num[idx:i])
                    if len(cur) < 2 or (len(cur) > 1 and cur[-1] + cur[-2] == n):

                        cur.append(n)
                       

                        if backtrack(i):
                            return True
                        cur.pop()

        return backtrack(0)