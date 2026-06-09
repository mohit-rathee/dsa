def spiral_traversal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (0, -1),  # left
        (-1, 0)   # up
    ]

    dir_idx = 0
    i = 0
    j = 0

    result = []

    for _ in range(rows * cols):
        result.append(matrix[i][j])

        di, dj = directions[dir_idx]
        ni = i + di
        nj = j + dj

        change_direction = False

        if dir_idx == 0 and nj > right:
            top += 1
            change_direction = True

        elif dir_idx == 1 and ni > bottom:
            right -= 1
            change_direction = True

        elif dir_idx == 2 and nj < left:
            bottom -= 1
            change_direction = True

        elif dir_idx == 3 and ni < top:
            left += 1
            change_direction = True

        if change_direction:
            dir_idx = (dir_idx + 1) % 4
            di, dj = directions[dir_idx]

        i += di
        j += dj

    return result


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(spiral_traversal(matrix))

