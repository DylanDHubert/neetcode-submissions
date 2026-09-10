class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def uP(i=0, j=0):
            if memo.get((i, j)): return memo[(i, j)]
            # BASE CASE (OOB)
            if (i == m) or (j == n): return 0
            # BASE CASE (END)
            if (i, j) == (m-1, n-1): return 1
            # UNIQUE PATHS FROM [a, b] = [a+1, b] + [a, b+1]
            unique_paths_from_here = uP(i+1, j) + uP(i, j+1)

            memo[(i, j)] = unique_paths_from_here
            return unique_paths_from_here

        return uP()




