class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        
        while matrix:
            
            #right to left
            
            arr += matrix.pop(0)
            
            
           
            if matrix and matrix[0]:
                # up to down
                for i in matrix:
                    arr.append(i.pop())
             # right to left      
            if matrix:
                arr += matrix.pop()[::-1]
            # down to up
            if matrix and matrix[0]:
                for i in matrix[::-1]:
                    arr.append(i.pop(0))

        return arr