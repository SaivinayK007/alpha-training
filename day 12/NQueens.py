from typing import List

class Solution:
    def __init__(self):
        self.ans = []
    
    def nqueens(self, n, r, col, tl, tr, b):
        if r == n:
            self.ans.append(b[:])  # Make a copy of the board
            return

        for c in range(n):
            if col[c] == 0 and tl[r - c + n - 1] == 0 and tr[r + c] == 0:
                row = list(b[r])         # Convert string to list for mutability
                row[c] = 'Q'
                b[r] = ''.join(row)

                col[c] = tl[r - c + n - 1] = tr[r + c] = 1
                self.nqueens(n, r + 1, col, tl, tr, b)
                row[c] = '.'             # Undo the move
                b[r] = ''.join(row)
                col[c] = tl[r - c + n - 1] = tr[r + c] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [0] * n
        tl = [0] * (2 * n - 1)   # top-left to bottom-right diagonals
        tr = [0] * (2 * n - 1)   # top-right to bottom-left diagonals
        b = ['.' * n for _ in range(n)]  # Create distinct row strings

        self.nqueens(n, 0, col, tl, tr, b)
        return self.ans
