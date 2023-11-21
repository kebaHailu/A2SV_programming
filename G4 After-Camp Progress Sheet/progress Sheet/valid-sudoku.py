class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        arr = []
        for idx , row in enumerate(board):
            for sec_idx , dgt in enumerate(row):
                if dgt != ".":
                    arr.extend([(dgt,idx),(sec_idx,dgt),(dgt,idx//3,sec_idx//3)])
        return (len(set(arr))==len(arr))

