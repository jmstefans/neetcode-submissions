class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # go through rows looking for duplicates
        for i in range(0,9):
            row = []
            for j in range(0,9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row:
                    return False
                else:
                    row.append(board[i][j])

        # go through columns looking for duplicates
        for i in range(0,9):
            col = []
            for j in range(0,9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in col:
                    return False
                else:
                    col.append(board[j][i])

        # go through 3x3 sub-boxes looking for duplicates
        for i in range(0,3):                # board sub-box X
            for j in range(0,3):            # board sub-box Y
                subBox = []
                for k in range(0,3):        # sub-box row index
                    for l in range(0,3):    # sub-box col index
                        if board[(3 * i) + k][(3 * j) + l] == '.':
                            continue
                        if board[(3 * i) + k][(3 * j) + l] in subBox:
                            return False
                        else:
                            subBox.append(board[(3 * i) + k][(3 * j) + l])

        # return true if we didn't find duplicates and didn't return false earlier
        return True