# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        g = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in g[j//3, i//3]:
                    return False
                else:
                    r[i].add(board[i][j])
                    c[j].add(board[i][j])
                    g[j//3, i//3].add(board[i][j])

        
        return True