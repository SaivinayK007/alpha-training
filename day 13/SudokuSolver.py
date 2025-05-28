from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        r, c, b = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        e = []
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == '.':
                    e.append((i, j))
                else:
                    r[i].add(v); c[j].add(v); b[i // 3 * 3 + j // 3].add(v)

        def vld(i, j, n):
            k = i // 3 * 3 + j // 3
            return n not in r[i] and n not in c[j] and n not in b[k]

        def bk(idx):
            if idx == len(e):
                return True
            i, j = e[idx]
            k = i // 3 * 3 + j // 3
            for n in '123456789':
                if vld(i, j, n):
                    board[i][j] = n
                    r[i].add(n); c[j].add(n); b[k].add(n)
                    if bk(idx + 1):
                        return True
                    r[i].remove(n); c[j].remove(n); b[k].remove(n); board[i][j] = '.'
            return False

        bk(0)