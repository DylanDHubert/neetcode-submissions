class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def path(i, j, index=1):
            if index == len(word): return 1
            found = 0
            letter = board[i][j]
            board[i][j] = "*"
            for delta_i, delta_j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_i, new_j = i+delta_i, j+delta_j
                if (-1 < new_i < rows) and (-1 < new_j < cols):
                    if board[new_i][new_j] == word[index]:
                        found += path(new_i, new_j, index=index+1)
            board[i][j] = letter
            return found

        # LOOP OVER POSTIONS
        rows, cols = len(board), len(board[0])

        found = False

        for i in range(rows):
            for j in range(cols):
                # WHEN FIRST LETTER FOUND
                if board[i][j] == word[0]:
                    if path(i, j):
                        return True

        return False

        # NEEDS BACKTRACKING...

