class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        array = [[0] * n for _ in range(m)]

        i, j = m-1, n-1

        array[i][j] = 1

        while (i > -1):
            while (j > -1):
                below, right = 0, 0
                if (i+1 <= m-1): below = array[i+1][j]
                if (j+1 <= n-1): right = array[i][j+1]
                array[i][j] += below + right
                j -= 1
            i -= 1
            j = n-1

        return array[0][0]
                
           

        