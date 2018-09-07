def DFS(i,j,visited, mat, row, col):
    nbr_row = [-1, -1, -1,  0, 0,  1, 1, 1]
    nbr_col = [-1,  0,  1, -1, 1, -1, 0, 1]

    visited[i][j] = True
    for k in range(len(nbr_row)):
        if ((i + nbr_row[k] >= 0) and \
            (j + nbr_col[k] >= 0) and \
            (i + nbr_row[k] < row) and \
            (j + nbr_col[k] < col) and
            (visited[i + nbr_row[k]][j + nbr_col[k]] == False) and \
            (mat[i + nbr_row[k]][j + nbr_col[k]] == 1)):

            DFS(i+nbr_row[k], j+nbr_col[k], visited, mat, row, col)

def zombieCluster(mat, row, col):

    is_visited = [[False for j in range(col)] for i in range(row)]

    count = 0
    for i in range(row):
        for j in range(col):
            if is_visited[i][j] == False and mat[i][j]==1:
                DFS(i,j,is_visited, mat, row, col)
                count += 1

    return count



if __name__ == '__main__':

    zombies = [[1, 1, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1]]
    row = len(zombies)
    col = len(zombies[0])

    result = zombieCluster(zombies, row, col)
    print(result)