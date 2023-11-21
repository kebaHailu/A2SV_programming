class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        row = len(matrix)
        col = len(matrix[0])

        top = left = 0
        right = col - 1
        bottom = row - 1


        res = [] 

        while len(res) < row * col:
            
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1 

            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -= 1


            if top <= bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom -= 1 
            
            if left <= right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left += 1
        
        return res
