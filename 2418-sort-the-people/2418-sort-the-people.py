class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}

        for i in range(len(names)) :

            dic[heights[i]] = names[i]


        max_bound = len(names)
        for i in range(len(names)):
            for j in range(i,len(names)):
                if heights[i] < heights[j]:
                    heights[i], heights[j] = heights[j],heights[i]
            
            max_bound -= 1
            
        arr = []

        for i in heights:
            arr.append(dic[i])

        return arr

