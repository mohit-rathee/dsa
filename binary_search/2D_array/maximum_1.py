def lower_bound(arr, n, x):
    low, high = 0, n

    while low < high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            high = mid
        else:
            low = mid + 1
    return low


def row_with_max_1s(matrix, n, m):
    count = 0
    index = -1

    for i in range(n):
        # Calculate count of 1s using lower bound
        ones_count = m - lower_bound(matrix[i], m, 1)
        if ones_count > count:
            count = ones_count
            index = i
    return index


matrix = [[1, 1, 1], [0, 1, 1], [0, 0, 0]]
n, m = 3, 3

ans = row_with_max_1s(matrix, n, m)
print(ans)
