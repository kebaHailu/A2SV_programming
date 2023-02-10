class Solution:
    def partitionLabels(self, s: str) -> List[int]:
       
    

        count = Counter(s)
        ans = []
        length = 0 
        check = set()

        for idx , val in enumerate(s):
            length += 1 
            check.add(val)
            count[val] -= 1 

            if count[val] == 0:
                check.remove(val)
                
                
                if len(check) == 0:
                    
                    ans.append(length)
                    length = 0
        return ans
