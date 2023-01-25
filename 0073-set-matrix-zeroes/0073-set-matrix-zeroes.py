class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        zeros = []
        for i in range(len(matrix)):

            if matrix[i].count(0) > 0:

                for idx , val in enumerate(matrix[i]):
                    if val == 0:
                        zeros.append(idx)
                matrix[i]= [0*n for n in range(len(matrix[i]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for k in zeros:
                    if j == k:
                        matrix[i][j] = 0