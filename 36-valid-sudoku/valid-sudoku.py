class Solution(object):
    def isValidSudoku(self, board):
        lines = board
        columns = []
        boxes = [[],[],[],[],[],[],[],[],[],[]]
        for line in range(9) : 
            aux = []
            for column in range(9) : 
                aux.append(board[column][line])
            columns.append(aux)
        for i in range(9) :
            for j in range(9):
                boxes[i//3+(j//3)*3].append(board[i][j]) 
        toVerify = lines + columns + boxes 
        for i in toVerify : 
            element = [j for j in i if j != '.'] 
            if len(set(element)) != len(element):
                return False
        return True



        