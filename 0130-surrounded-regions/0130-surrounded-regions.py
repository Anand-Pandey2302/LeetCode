class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        stack = []

        # Boundary ke O ko safe mark karo
        for i in range(m):
            if board[i][0] == 'O':
                stack.append((i, 0))
            if board[i][n - 1] == 'O':
                stack.append((i, n - 1))

        for j in range(n):
            if board[0][j] == 'O':
                stack.append((0, j))
            if board[m - 1][j] == 'O':
                stack.append((m - 1, j))

        # Iterative DFS
        while stack:
            r, c = stack.pop()

            if board[r][c] != 'O':
                continue

            board[r][c] = '#'

            if r > 0 and board[r - 1][c] == 'O':
                stack.append((r - 1, c))

            if r < m - 1 and board[r + 1][c] == 'O':
                stack.append((r + 1, c))

            if c > 0 and board[r][c - 1] == 'O':
                stack.append((r, c - 1))

            if c < n - 1 and board[r][c + 1] == 'O':
                stack.append((r, c + 1))

        # Final board update
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'