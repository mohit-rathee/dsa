def rotate_matrix(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            # Swap element at (i, j) with (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        # Reverse the current row to simulate clockwise rotation
        matrix[i].reverse()

    for r in matrix:
        print(r)


matrix = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
rotate_matrix(matrix)
