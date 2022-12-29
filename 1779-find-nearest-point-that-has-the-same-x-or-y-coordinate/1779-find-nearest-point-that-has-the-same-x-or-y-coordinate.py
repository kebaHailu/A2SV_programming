class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        mystr =[]
        min_val = float('inf')
        for i in points:
            if i[0] == x or i[1]== y:

                min_val = min( min_val , (abs(i[0]-x) + abs(i[1]-y)) )

        for i in points:
            if abs(i[0]-x)+abs(i[1]-y) == min_val and (i[0] == x or i[1]== y ):

                return points.index(i)
            
        
        return -1


