class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r * c or (len(mat)==r and len(mat[0]) == c):
            return mat
        else:
            arr =[]
            new_mat = [[0]*c for _ in range(r)]
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    arr.append(mat[i][j])
            x = 0      
            for i in range(r):
                for j in range(c):
                    new_mat[i][j] = arr[x]
                    x += 1
            return new_mat
                    