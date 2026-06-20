def upper_bound(row, val):
    low, high = 0, len(row)
    while low < high:
        mid = (low + high) // 2
        if row[mid] > val:
            high = mid
        else:
            low = mid + 1
    return low


def findMedian(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)

    while low < high:
        mid = (low + high) // 2
        count = 0

        for row in matrix:
            count += upper_bound(row, mid)

        if count < (rows * cols + 1) // 2:
            low = mid + 1
        else:
            high = mid

    return low


matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
ans = findMedian(matrix)
print(ans)
