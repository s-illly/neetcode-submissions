class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)


        for i in range(9):
            for j in range(9):
                sq_index = ((i // 3) * 3) + (j // 3)
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                if board[i][j] in square[sq_index]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                square[sq_index].add(board[i][j])
        return True

                
            