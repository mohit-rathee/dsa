def set_zeroes_hashset(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    for r in range(rows):
        for c in range(cols):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0

    return matrix


def set_zeroes_optimal(matrix):
    # -----------------------------
    # Space: O(1)
    # -----------------------------
    rows = len(matrix)
    cols = len(matrix[0])

    is_first_row_zero = False
    is_first_col_zero = False

    # Check if first row contains any 0
    for c in range(cols):
        if matrix[0][c] == 0:
            is_first_row_zero = True
            break

    # Check if first column contains any 0
    for r in range(rows):
        if matrix[r][0] == 0:
            is_first_col_zero = True
            break

    # Mark rows and columns using first row and first column
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    # Update matrix excluding first row and first column
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if is_first_row_zero:
        for c in range(cols):
            matrix[0][c] = 0

    if is_first_col_zero:
        for r in range(rows):
            matrix[r][0] = 0

    return matrix


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# set_zeroes_hashset(matrix)
set_zeroes_optimal(matrix)
print(matrix)
