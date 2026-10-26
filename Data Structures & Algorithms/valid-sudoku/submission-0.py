class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkValid(part):
            contains = dict()
            for i in part:
                if i == ".":
                    continue
                else:
                    if i in contains:
                        return False
                    else:
                        contains[i] = 1
            return True
        
        res = True

        while res == True:
            for i in range(len(board)):
                res = res and checkValid(board[i])
                res = res and checkValid([row[i] for row in board])
            for i in range(0,9,3):
                for j in range(0,9,3):
                    square = []
                    for k in range(3):
                        square += list(board[j+k][i:i+3])
                    res = res and checkValid(square)
            return res
        return res
                    
                
