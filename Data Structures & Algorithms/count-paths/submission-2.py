class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array = [1] * n
        
        for _ in range(m-1):
            index = n - 2
            while index > -1:
                array[index] += array[index+1]
                index -= 1
        

        return array[0]
        