def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = n * m - 1

    while low <= high:
        mid = (low + high) // 2

        row = mid // m
        col = mid % m

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

ans = searchMatrix(matrix, 8)
print(ans)
