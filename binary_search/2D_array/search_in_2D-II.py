def search_element(matrix, target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])

    row = 0
    col = m - 1

    while row < n and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True
        elif current < target:
            row += 1
        else:
            col -= 1

    return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]

ans = search_element(matrix, 18)
print(ans)
