class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = {}
        cols = {}
        squares = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                else:
                    if i not in rows:
                        rows[i] = set()
                    if j not in cols:
                        cols[j] = set()

                    box_key = (i // 3, j // 3)
                    if box_key not in squares:
                        squares[box_key] = set()

                    if (board[i][j] in rows[i] or 
                        board[i][j] in cols[j] or 
                        board[i][j] in squares[box_key]):
                        return False

                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[box_key].add(board[i][j])

        return True