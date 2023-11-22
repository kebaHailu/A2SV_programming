class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xlist = [i[0] for i in coordinates]
        ylist = [j[1] for j in coordinates]
        x0,y0 = coordinates[0]
        x1,y1 = coordinates[1]
        def stright(x,y):
            nonlocal x0,y0,x1,y1
            if y1 - y0 == 0:
                return len(set(ylist)) == 1
            ycal = y1-y0
            if x1 - x0 == 0:
                return len(set(xlist)) == 1
            ycal /= x1-x0
            ycal *= ( x - x0)
            ycal += y0
            
            return y == ycal


        for i in range(2,len(coordinates)):
            x , y = coordinates[i]
            if not stright(x,y):
                return False 
        

        return True 