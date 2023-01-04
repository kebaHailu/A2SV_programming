class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row = grid
        colmn = []
        cont = 0

        for i in range(len(row)):
            col = []
            for j in range(len(row)):

                col.append(row[j][i])

            colmn.append(col)


        for i in row:
            for j in colmn:
                if i == j :
                    cont += 1

        return cont
