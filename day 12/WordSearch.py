class Solution:
    def dfs(self, b, i, j, k, s):
        if k == len(s):
            self.state = True
            return
        if i < 0 or j < 0 or i >= len(b) or j >= len(b[0]) or b[i][j] != s[k]:
            return

        temp = b[i][j]
        b[i][j] = '#'  # Mark as visited

        self.dfs(b, i - 1, j, k + 1, s)
        self.dfs(b, i + 1, j, k + 1, s)
        self.dfs(b, i, j - 1, k + 1, s)
        self.dfs(b, i, j + 1, k + 1, s)

        b[i][j] = temp  # Restore character

    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    self.state = False  # Reset before each new DFS
                    self.dfs(board, i, j, 0, word)
                    if self.state:
                        return True  # Found a path

        return False  # No path found

        