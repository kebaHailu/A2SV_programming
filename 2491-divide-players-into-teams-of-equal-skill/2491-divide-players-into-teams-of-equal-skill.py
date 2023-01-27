class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill)-1
        arr =[]
        while i < j:
            arr.append([skill[i],skill[j]])
            i += 1
            j -= 1
        if len(skill)//2 == len(arr) :
            newsum = 0
            mysum = skill[0] + skill[-1]
            if all([mysum == sum(subarr) for subarr in arr]):
                for i in arr:
                    newsum += i[0] * i[1]
                return newsum
            else:
                return -1
            
     
        else:
            return -1
            