from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        colu = defaultdict(set)
        grid = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row[i] or board[i][j] in colu[j] or board[i][j] in grid[(i//3, j//3)]:
                    return False
                row[i].add(board[i][j])
                colu[j].add(board[i][j])
                grid[(i//3, j//3)].add(board[i][j])

        return True