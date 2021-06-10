# given a matrix, 1 represents island, and 0 represents water 
# remove all islands that are not connected to the borders of the matrix 


    

def removeislands(matrix):
    border_islands = {}
    def dfs(matrix,i, j):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]) and matrix[i][j]:
            if (i,j) not in border_islands:
                border_islands[(i,j)] = True
            dfs(matrix, i+1, j)
            dfs(matrix,  i-1, j)
            dfs(matrix, i, j+1)
            dfs(matrix, i, j-1)
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] and (i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix[0])-1):
                dfs(matrix, i, j) 

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] and (i,j) not in border_islands:
    
                matrix[i][j] = 0
    
    

    return matrix

matrix = [[1, 1, 0, 0, 0],
         [0, 1, 0, 1, 0],
         [1, 0, 0, 0, 1],
         [0, 1, 0, 0, 0],
         [1, 0, 1, 0, 1]]

testedmat = removeislands(matrix)
for i in range(len(testedmat)):
    print(testedmat[i])
    