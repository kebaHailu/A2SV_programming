class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
       
        arr.sort()
        for i in arr:
            if i*2 in arr and i !=0 :
                return True 

            elif i == 0:
                if arr.count(0) > 1:
                    return True

        return False
