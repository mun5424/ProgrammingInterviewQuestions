# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = 0
        matrix = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1): 
                if i == m-1 or j == n-1:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
        print(matrix)
        return matrix[0][0]
    