class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        

        set_queens = set()
        for i in queens:
            set_queens.add((i[0],i[1]))
        possible = []

        # up
        for i in range(king[0],-1,-1):
            if (i,king[1]) in set_queens:
                possible.append([i,king[1]])
                break

        # down 
        for i in range(king[0],8):

            if (i,king[1]) in set_queens:
                possible.append([i,king[1]])
                break

        # right
        for i in range(king[1],8):
            if (king[0],i) in set_queens:
                possible.append([king[0],i])
                break

        # left
        for i in range(king[1],-1,-1):
            if (king[0],i) in set_queens:
                possible.append([king[0],i])
                break

        i = king[0]
        j = king[1]

        while i < 8 and j < 8:
            if (i,j) in set_queens:
                possible.append([i,j])

                break
            i += 1
            j += 1
        i = king[0]
        j = king[1]    
        while i > -1 and j < 8:
            if (i,j) in set_queens:
                possible.append([i,j])

                break
            i -= 1
            j += 1
        i = king[0]
        j = king[1]   
        while i < 8 and j > -1:
            if (i,j) in set_queens:
                possible.append([i,j])

                break
            i += 1
            j -= 1
        i = king[0]
        j = king[1]    
        while i > -1 and j > -1:
            if (i,j) in set_queens:
                possible.append([i,j])
               
                break
            i -= 1
            j -= 1



        return possible